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
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }
    return render(request, 'Game/AvAl_MainPage_extender.html', context)


def about(request):
    return render(request, 'Game/about.html', {"menu": menu, 'title': 'О разработчике'})


def library(request):
    cats = Category.objects.all()

    context = {
        'menu': menu,
        'title': 'Библиотека',
        'cats': cats
    }
    return render(request, 'game/library.html', context)


def login(request):
    return HttpResponse('Авторизация')


def library_mobs(request):
    posts = mobs.objects.all()

    context = {
        'menu': menu,
        'title': 'Библиотека',
        'posts': posts
    }
    return render(request, 'game/library.html', context)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с id = {cat_id}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page is FUCKED</h2>')
