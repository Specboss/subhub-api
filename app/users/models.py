from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Пользователь
    """
    ROLE_CHOICES = [
        ('author', 'Автор'),
        ('user', 'Пользователь'),
    ]

    first_name = models.CharField("Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField("Фамилия", max_length=50, blank=True, null=True)
    second_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    email = models.EmailField('E-mail адрес', unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='Роль пользователя'
    )

    tg_user_id = models.BigIntegerField("Telegram ID", null=True, blank=True, db_index=True)
    tg_username = models.CharField("Telegram username", max_length=100, blank=True, null=True, db_index=True)
    tg_first_name = models.CharField("Telegram имя", max_length=100, blank=True, null=True)
    tg_last_name = models.CharField("Telegram фамилия", max_length=100, blank=True, null=True)

    inn = models.CharField(verbose_name='ИНН', max_length=12, null=True, blank=True, db_index=True)

    about = models.TextField(verbose_name='Описание', blank=True, null=True)

    updated_at = models.DateTimeField("Дата последнего обновления", auto_now=True)
    created_at = models.DateTimeField("Дата регистрации", auto_now_add=True)
    groups = models.ManyToManyField(
            'auth.Group',
            related_name='custom_user_set',
            blank=True,
            help_text="Группы, к которым принадлежит этот пользователь.",
            verbose_name="Группы"
        )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text="Конкретные разрешения для этого пользователя.",
        verbose_name="Права пользователя"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name}"
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"