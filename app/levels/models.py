from django.db import models
from django.core import validators

from app.users.models import User

class Level(models.Model):
    """
    Уровни подписок автора
    """
    CURRENCY_CHOICES = [
        ('RUB', 'Рубль'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validators.MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class LevelUser(models.Model):
    """
    Подписка обычного пользователя на автора
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='Обычный пользователь', db_index=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} подписан на {self.level}"
