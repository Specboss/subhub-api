from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import filters
from drf_api import auth_permission
from app.post_feedbacks import models
from app.posts.models import Post

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('level').prefetch_related('comments', 'postlike_set', 'attachments')
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [IsAuthenticated(), auth_permission.Author()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save()

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = models.PostLike.objects.all()
    serializer_class = serializers.PostLikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.validated_data['post']
        if models.PostLike.objects.filter(user=user, post=post).exists():
            raise ValidationError('You already liked this post.')
        serializer.save(user=user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all().select_related('post', 'user').prefetch_related('reactions')
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentReactionViewSet(viewsets.ModelViewSet):
    queryset = models.CommentReaction.objects.all()
    serializer_class = serializers.CommentReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        comment = serializer.validated_data['comment']
        if models.CommentReaction.objects.filter(user=user, comment=comment).exists():
            raise ValidationError('You already reacted to this comment.')
        serializer.save(user=user)