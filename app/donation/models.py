from django.utils import timezone
from django.core import validators
from django.db import models

from app.users.models import User

class Donation(models.Model):
    """
    Донаты
    """
    CURRENCY_CHOICES = [
        ('RUB', 'Рубль'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=False)
    title = models.CharField(max_length=255, default='Мой крутой донат')
    description = models.TextField()
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validators.MinValueValidator(0)]
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
    is_active = models.BooleanField(default=True)

    closed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def close(self):
        """
        Закрыть сбор доната
        """
        self.is_active = False
        self.closed_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} ({self.amount} {self.currency})"

class UserDonation(models.Model):
    """
    Связка донатов и озера
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_index=True)
    donate = models.ForeignKey(Donation, on_delete=models.CASCADE, null=False, db_index=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validators.MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username