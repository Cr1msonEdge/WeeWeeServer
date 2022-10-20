from django import forms
from .models import *


class AddCommForm(forms.Form):
    title = forms.CharField(max_length=255, label='Имя моба', widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label='Кодовое имя')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                              label='Описание')
    is_published = forms.BooleanField(label="Опубликовать", required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label="Категория существа", empty_label='Категория не выбрана')
