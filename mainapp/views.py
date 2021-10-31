from django.shortcuts import render
from .models import CollectionCategory, Champion, Skin
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'mainapp/index.html', context=context)


def collection(request, pk=None):
    context = {
        'title': 'Collection',
        'categories': CollectionCategory.objects.all(),
        'champions': Champion.objects.all()
    }
    return render(request, 'mainapp/collection.html', context=context)


def store(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'mainapp/store.html', context=context)


links_menu = [
    {'url': 'loot_chests',
    'title': 'Materials',
    'img': 'img/Loot_chests.svg'},
    {'url': 'loot_champs',
    'title': 'Champions',
    'img': 'img/Loot_champs.svg'},
    {'url': 'loot_skins',
    'title': 'Skins',
    'img': 'img/Loot_skins.svg'},
    {'url': 'loot_emotes',
    'title': 'Emotes',
    'img': 'img/Loot_emotes.svg'},
    {'url': 'loot_wards',
    'title': 'Ward Skins',
    'img': 'img/Loot_wards.svg'},
    {'url': 'loot_icons',
    'title': 'Icons',
    'img': 'img/Loot_icons.svg'}
]


def loot(request):
    context = {
        'links_menu': links_menu,
        'title': 'Loot',
    }
    return render(request, 'mainapp/loot.html', context=context)


def loot_chests(request):
    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/loot_chests.html', context=context)


def loot_champs(request):
    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/loot_champs.html', context=context)


def loot_skins(request):
    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/loot_skins.html', context=context)


def loot_emotes(request):
    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/loot_emotes.html', context=context)


def loot_wards(request):
    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/loot_wards.html', context=context)


def loot_icons(request):
    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/loot_icons.html', context=context)
