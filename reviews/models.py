from django.db import models
from users.models import User


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ("id",)

    def __str__(self):
        return f"{self.user}"

    @classmethod
    def search(cls, query):
        return cls.objects.filter(description__icontains=query)
