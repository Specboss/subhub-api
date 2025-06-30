from django.core import validators
from django.db import models
from kombu.transport.native_delayed_delivery import level_name

from app.levels.models import Level


class Post(models.Model):
    """
    Пост автора
    """
    level = models.ForeignKey(Level, verbose_name='Уровень', on_delete=models.CASCADE, null=False, db_index=True)
    title = models.CharField(verbose_name='Заголовок', max_length=1024, null=False, blank=False, default='Новый пост')
    description = models.TextField(verbose_name='Описание')
    can_comment = models.BooleanField(verbose_name='Комменатрии включены?', default=True)
    is_ads = models.BooleanField(verbose_name='Реклама?', default=False)
    support_amount = models.DecimalField(verbose_name='Минимальная сумма поддержки', max_digits=10, decimal_places=2, validators=[validators.MinValueValidator(0)])
    currency = models.CharField(verbose_name='Валюта', max_length=3, choices=Level.CURRENCY_CHOICES, default='RUB')
    is_pin = models.BooleanField(verbose_name='Закреплена?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Пост: {self.title} - Автор: {self.level.author.username}'