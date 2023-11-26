from django.urls import path
from .views import user_logout, create_profile, edit_profile, delete_profile, user_login, index

app_name = 'profiles'

urlpatterns = [
    # path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('create/', create_profile, name='create_profile'),
    path('<str:username>/edit/', edit_profile, name='edit_profile'),
    path('<str:username>/delete/', delete_profile, name='delete_profile'),
    path('logout/', user_logout, name='logout'),
]
