from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О разработчике', 'url_name': 'about'},
        {'title': 'Авершин', 'url_name': 'Avershin'},
        {'title': 'Предложения', 'url_name': 'addcomment'},
        {'title': 'Регистрация', 'url_name': 'register'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('mobs'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
