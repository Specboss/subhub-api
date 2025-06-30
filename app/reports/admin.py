from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('post__title', 'user__username')  # Предполагается, что у Post есть title, а у UserWarning — username
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('post', 'user', 'status')
        }),
        ('Дополнительно', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )