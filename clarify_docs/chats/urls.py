from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.main, name='main'),
    path('chats/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    # path('<int:chat_id>/ask/', views.ask, name='ask'),
]