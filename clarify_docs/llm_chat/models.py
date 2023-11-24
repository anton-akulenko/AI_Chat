from django.db import models
from django.contrib.auth.models import User
from clarify_docs import settings

User = settings.AUTH_USER_MODEL


class CustomProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'llm_chat'


class PDFDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # document = models.FileField(upload_to='pdf_documents/')
    documentContent = models.TextField(null=True, blank=True)
    embedding = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s PDF: {self.document.name}"

    class Meta:
        app_label = 'llm_chat'


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_document = models.ForeignKey(PDFDocument, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    # question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} at {self.timestamp}: Q: {self.question}, A: {self.answer}"

    class Meta:
        app_label = 'llm_chat'


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_files_uploaded = models.IntegerField(default=0)
    total_questions_asked = models.IntegerField(default=0)

    class Meta:
        app_label = 'llm_chat'
