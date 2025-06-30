from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'second_name', 'tg_user_id', 'tg_username'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password1'):
            user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User

    list_display = (
        'id', 'email', 'first_name', 'last_name', 'tg_user_id', 'tg_username', 'created_at'
    )
    list_filter = ('created_at', 'is_staff', 'is_superuser', 'groups')
    search_fields = ('email', 'first_name', 'last_name', 'tg_username', 'tg_user_id')
    ordering = ('-created_at',)
    list_editable = ('first_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Личная информация', {
            'fields': ('first_name', 'last_name', 'second_name', 'about')
        }),
        ('Telegram данные', {
            'fields': ('tg_user_id', 'tg_username', 'tg_first_name', 'tg_last_name')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'second_name',
                'tg_user_id', 'tg_username'
            ),
        }),
    )

    list_per_page = 25