from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

# Create your views here.

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О разработчике', 'url_name': 'about'},
        {'title': 'Авершин', 'url_name': 'Avershin'},
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
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Разработчик',
        'cats': cats
    }
    return render(request, 'Game/about.html', context=context)


def library(request):
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Библиотека',
        'cats': cats
    }
    return render(request, 'game/library.html', context=context)


def login(request):
    return HttpResponse('Авторизация')


def Avershin(request):
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Библиотека',
        'cats': cats
    }
    return render(request, 'game/avershin.html', context=context)


def library_mobs(request):
    posts = mobs.objects.all()
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Библиотека',
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'game/library.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(mobs, slug=post_slug)
    cat = Category.objects.get(pk=post.cat_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': cat.slug,
    }

    return render(request, 'game/post.html', context=context)


def show_category(request, cat_slug):
    cats = Category.objects.all()
    cat = Category.objects.get(slug=cat_slug)
    posts = mobs.objects.filter(cat=cat.pk)

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat.slug,
    }

    return render(request, 'game/library.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page is FUCKED</h2>')
