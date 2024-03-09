from django.db import models
from users.models import User
from django.db.models import Q
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    @classmethod
    def search(cls, query):
        return cls.objects.filter(category__name__icontains=query)


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'note'
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ("id",)

    def __str__(self):
        return f"{self.user}"

    @classmethod
    def search(cls, query):
        return cls.objects.filter(Q(description__icontains=query))
