from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import CreateUserForm


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'main/register_page.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog')

    context = {
        'title': 'Вход',
    }
    return render(request, 'main/login_page.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def welcome_page(request):
    context = {
        'title': 'Приветственная страница',
    }
    return render(request, 'main/welcome_page.html', context)


@login_required
def blog_page(request):
    context = {
        'title': 'Блог',
    }
    return render(request, 'main/blog_page.html', context)


@login_required
def dog_post_page(request):
    context = {
        'title': 'Пост про собак',
    }
    return render(request, 'main/dog_post_page.html', context)
