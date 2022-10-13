from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

# Create your views here.

menu = ['О сайте', 'Добавить моба', 'Обратная связь', 'Войти']


def mainPage(request):
    return HttpResponse("<h1>Главная страница</h1>")


def index(request):  # HttpRequest
    posts = mobs.objects.all()
    return render(request, 'Game/index.html', {'posts': posts, "menu": menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'Game/about.html', {"menu": menu, 'title': 'О сайте'})


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def categories(request, regslug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Страница регистрации</h1><p>{regslug}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page is FUCKED</h2>')
