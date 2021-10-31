from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from authapp.forms import PlayerLoginForm, PlayerRegisterForm, PlayerEditForm


def index(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth:login'))


def login(request):
    login_form = PlayerLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        player = auth.authenticate(username=username, password=password)
        if player and player.is_active:
            auth.login(request, player)
            return HttpResponseRedirect(reverse('home'))
    context = {
        'login_form': login_form
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth:login'))


def register(request):
    if request.method == 'POST':
        register_form = PlayerRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        register_form = PlayerRegisterForm()

    context = {
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', context)


def edit(request):
    if request.method == 'POST':
        edit_form = PlayerEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        edit_form = PlayerEditForm(instance=request.user)

    context = {
        'edit_form': edit_form
    }
    return render(request, 'authapp/edit.html', context)
