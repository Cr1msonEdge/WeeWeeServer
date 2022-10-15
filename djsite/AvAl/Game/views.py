from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

# Create your views here.

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О разработчике', 'url_name': 'about'},
        {'title': 'Библиотека', 'url_name': 'library'},
        {'title': 'Вход', 'url_name': 'login'}
        ]


def mainPage(request):
    return HttpResponse("<h1>Главная страница</h1>")


def index(request):  # HttpRequest
    posts = mobs.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'Game/AvAl_MainPage_extender.html', context)


def about(request):
    return render(request, 'Game/about.html', {"menu": menu, 'title': 'О разработчике'})


def library(request):
    posts = mobs.objects.all()
    context = {
        'menu': menu,
        'title': 'Библиотека',
        'posts': posts
    }
    return render(request, 'game/library.html', context)


def login(request):
    return HttpResponse('Авторизация')


def library_mobs(request):
    posts = mobs.objects.all()
    return render(request, 'game/AvAl_library.html', {'posts': posts})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page is FUCKED</h2>')
