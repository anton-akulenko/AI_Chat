from io import BytesIO
from os.path import splitext
from abc import abstractclassmethod, ABC

import pdfplumber
from docx2txt import process
from django.core.files.uploadedfile import InMemoryUploadedFile


class Reader(ABC):

    @abstractclassmethod
    def read(self, file: InMemoryUploadedFile) -> str:
        pass


class PDFReader(Reader):

    def read(self, file: InMemoryUploadedFile) -> str:
        text = ""
        in_memory_pdf = BytesIO(file.read())
        with pdfplumber.open(in_memory_pdf) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text

class TXTReader(Reader):

    def read(self, file: InMemoryUploadedFile) -> str:
        text = file.file.read()
        return text.decode("utf-8")


class DOCXReader(Reader):

    def read(self, file: InMemoryUploadedFile) -> str:
        text = process(file.file)
        return text
    

READERS = {'.pdf': PDFReader(), '.txt': TXTReader(), '.docx': DOCXReader()}


def read_file(file: InMemoryUploadedFile) -> str:
    filename = file.name
    _, file_extension = splitext(filename)

    try:
        reader = READERS[file_extension]
    except KeyError as e:
        return None
    
    return reader.read(file)
    

def normalize_filename(filename):
    filename = filename.replace(" ", "_")
    filename = filename.lower()
    return filename