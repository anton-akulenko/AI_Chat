from django.contrib import admin
from .models import CustomProfile, PDFDocument, ChatMessage, UserData
# Register your models here.
admin.site.register(CustomProfile)
admin.site.register(PDFDocument)
admin.site.register(ChatMessage)
admin.site.register(UserData)