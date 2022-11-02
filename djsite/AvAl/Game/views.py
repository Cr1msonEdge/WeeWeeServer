from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
from .utils import *


# Create your views here.


class Home(DataMixin, ListView):
    model = mobs
    template_name = 'game/AvAl_MainPage_extender.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return mobs.objects.filter(is_published=True)


class MobsCategory(DataMixin, ListView):
    model = mobs
    template_name = 'game/AvAl_MainPage_extender.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' +
                                            str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return mobs.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class ShowPost(DataMixin, DetailView):
    model = mobs
    template_name = 'game/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCommForm
    template_name = 'game/addcomment.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Предложения")
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Разработчик',
        'cats': cats
    }
    return render(request, 'Game/about.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'game/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

# def index(request):  # HttpRequest
#     posts = mobs.objects.all()
#     cats = Category.objects.all()
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0
#     }
#     return render(request, 'Game/AvAl_MainPage_extender.html', context=context)


def mainPage(request):
    return HttpResponse("<h1>Главная страница</h1>")


# def addcomment(request):
#     if request.method == 'POST':
#         form = AddCommForm('POST')
#         if form.is_valid():
#             #  print(form.cleaned_data)
#             try:
#                 mobs.object.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления отзыва')
#     else:
#         form = AddCommForm()
#     context = {
#         'menu': menu,
#         'title': 'Предложить персонажа',
#         'form': form,
#     }
#     return render(request, 'Game/addcomment.html', context=context)


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
        'title': 'Александр Сергеевич Авершин',
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


# def show_post(request, post_slug):
#     post = get_object_or_404(mobs, slug=post_slug)
#     cat = Category.objects.get(pk=post.cat_id)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': cat.slug,
#     }
#
#     return render(request, 'game/post.html', context=context)


# def show_category(request, cat_slug):
#     cats = Category.objects.all()
#     cat = Category.objects.get(slug=cat_slug)
#     posts = mobs.objects.filter(cat=cat.pk)
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Отображение по категориям',
#         'cat_selected': cat.slug,
#     }
#
#     return render(request, 'game/library.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page is FUCKED</h2>')
