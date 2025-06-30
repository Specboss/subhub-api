from django.db import models

from app.posts.models import Post
from app.users.models import User


class Report(models.Model):
    """
    Жалобы на посты авторов
    """
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('pending', 'На рассмотрении'),
        ('rejected', 'Отклонено'),
        ('resolved', 'Решено'),
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Пост', db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Пользователь', db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"Жалоба на {self.post} — {self.get_status_display()}"

