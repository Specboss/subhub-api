from django.db import models

from app.posts.models import Post
from app.users.models import User


class PostLike(models.Model):
    """
    Лайки к постам
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_index=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user} liked {self.post}"

class Comment(models.Model):
    """
    Комменатрии
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"

class CommentReaction(models.Model):
    """
    Реакции к комментариям
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_index=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=False, related_name='reactions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')

    def __str__(self):
        return f"{self.user} liked comment {self.comment.id}"

