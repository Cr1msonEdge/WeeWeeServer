from django.db import models

# Create your models here.
from django.urls import reverse


class mobs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Информация')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Изображение')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=True, verbose_name='Выложено')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'персонаж'
        verbose_name_plural = 'персонажи'
        ordering = ['time_created', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
