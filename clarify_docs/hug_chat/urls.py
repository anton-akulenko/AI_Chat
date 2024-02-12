from django.urls import path
from . import views

urlpatterns = [
    path('hug_chat/', views.hug_chat, name='hug_chat'),
]