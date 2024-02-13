from transformers import AutoTokenizer, pipeline, AutoModelForQuestionAnswering

from .elasticsearch_crud import get_context

MODEL = AutoModelForQuestionAnswering.from_pretrained('henryk/bert-base-multilingual-cased-finetuned-dutch-squad2')

class QAModel:

    def __init__(self, context_id: str, max_length: int = 1024) -> None: 
        self.max_length = max_length
        self.model_name = 'henryk/bert-base-multilingual-cased-finetuned-dutch-squad2'
        self.context = get_context(context_id)

    def tokenize_question(self, question: str, truncation: bool = True, padding: bool = True):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        tokenizer.encode(question, truncation = truncation, padding = padding, max_length = self.max_length)
        return tokenizer

    def create_pipeline(self, tokenizer, model):
        nlp = pipeline('question-answering', model, tokenizer=tokenizer)
        return nlp

    def get_answer(self, question: str, truncation: bool = True, padding: bool = True) -> dict:
        tokenizer = self.tokenize_question(question, truncation, padding)
        model_pipeline = self.create_pipeline(tokenizer, MODEL)
        answer = model_pipeline(question = question, context = self.context, max_length = self.max_length)
        return answer['answer']
    


