from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import RegisterForm, LoginForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def create_profile(request):
    if request.user.is_authenticated:
        return redirect(to='base')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='profiles:index')
        else:
            return render(request, 'create_profile.html', context={"form": form})

    return render(request, 'create_profile.html', context={"form": RegisterForm()})


def user_login(request):
    if request.user.is_authenticated:
        return redirect(to='base')

    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='profiles:login')

        auth_login(request, user)
        return redirect(to='llm_chat:home')

    return render(request, 'login.html', context={"form": LoginForm()})


@login_required
def edit_profile(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form, 'user_profile': user_profile})


@login_required
def delete_profile(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)

    if request.user == user_profile:
        user_profile.delete()
        return redirect('llm_chat:home')
    else:
        return redirect('llm_chat:home')


def user_logout(request):
    logout(request)
    return redirect('llm_chat:home')
