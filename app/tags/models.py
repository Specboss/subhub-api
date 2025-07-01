from django.db import models

from app.posts.models import Post
from app.users.models import User

class Tag(models.Model):
    """
    Кастомные теги автора
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TagPost(models.Model):
    """
    Привязка тега к посту
    """
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False, db_index=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PreparedTag(models.Model):
    """
    Встроенные теги
    """
    title = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title