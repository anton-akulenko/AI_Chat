from django.contrib import admin
from django.urls import path

from . import views

app_name = 'llm_chat'

from . import views



urlpatterns = [
    path('', views.main, name='home'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('get_chat_history/', views.get_chat_history, name='get_chat_history'),
]


# urlpatterns = [
#     path('', views.main, name='home'),
#     path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
#     path('ask_question/', views.ask_question, name='ask_question'),
#     path('get_chat_history/', views.get_chat_history, name='get_chat_history'),
#     # path('new_chat/', new_chat, name='new_chat'),
#     # path('error-handler/', error_handler, name='error_handler'),

# ]