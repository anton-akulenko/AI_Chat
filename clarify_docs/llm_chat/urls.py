from django.contrib import admin
from django.urls import path

from .views import upload_pdf, ask_question, get_chat_history, main #new_chat, error_handler,

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', main, name='home'),
    path('upload_pdf/', upload_pdf, name='upload_pdf'),
    path('ask_question/', ask_question, name='ask_question'),
    path('get_chat_history/', get_chat_history, name='get_chat_history'),
    # path('new_chat/', new_chat, name='new_chat'),
    # path('error-handler/', error_handler, name='error_handler'),

]