from django.db import models
from django.core.files.storage import storages

from app.posts.models import Post

def upload_to_attachments(instance, filename):
    return f"posts/{instance.id}/{filename}"

class Attachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='attachments', null=False, db_index=True)
    file = models.FileField(
        upload_to=upload_to_attachments,
        null=True,
        blank=True,
        verbose_name='Вложения',
        storage=storages["minio"]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Вложения для поста номер {self.post.id}'