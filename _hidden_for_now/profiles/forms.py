from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'type': 'email'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())

    class Meta:
        model = UserProfile 
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'bio']
