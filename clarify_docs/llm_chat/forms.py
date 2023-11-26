from django import forms
from django.forms import FileInput
from .models import PDFDocument, ChatMessage, CustomProfile
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomProfile
        fields = ('phone', 'address')


class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'embedding']


class PDFDocumentForm2(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'documentContent', 'embedding']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'documentContent': forms.Textarea(attrs={'class': 'form-control'}),
            'embedding': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'documentContent': 'Document Content',
            'embedding': 'Embedding',
        }


class PDFUpdateForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'documentContent', 'embedding']


class PDFUploadForm(forms.Form):
    pdf_document = forms.FileField(label='Upload a PDF', required=True, widget=FileInput({'class': "form-control"}))


class UserQuestionForm(forms.Form):
    user_question = forms.CharField(max_length=255, label='Your Question')
