from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, mixins

from . import serializers
from app.levels.models import Level, LevelUser
from drf_api import auth_permission
from drf_api.paginators import InfinitePagination


class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = serializers.LevelSerializer
    permission_classes = [IsAuthenticated, auth_permission.Author]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['price']
    ordering = ['price']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListLevelsAPIView(ListAPIView):
    serializer_class = serializers.LevelSerializer
    permission_classes = [IsAuthenticated, auth_permission.User]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['price']
    ordering = ['price']

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        return Level.objects.filter(author_id=author_id)

class AuthorSubscribersViewSet(mixins.ListModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    """
    Просмотр и удаление подписчиков автора
    """
    permission_classes = [auth_permission.Author, IsAuthenticated]
    pagination_class = InfinitePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def get_queryset(self):
        return (
            LevelUser.objects
            .filter(level__author=self.request.user)
            .select_related('level', 'user')
            .annotate(
                username=F('user__username'),
                email=F('user__email'),
                level=F('level__title'),
                price=F('level__price'),
            )
        )

class UserSubscriptionsApiView(viewsets.ModelViewSet):
    """
    Пользователь:
    - подписываться
    - отменять подписку
    - просматривать свои подписки
    """
    serializer_class = serializers.LevelSerializer
    permission_classes = [IsAuthenticated, auth_permission.User]
    pagination_class = InfinitePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def get_queryset(self):
        return (
            LevelUser.objects
            .filter(user=self.request.user)
            .select_related('level', 'level__author')
            .annotate(
                level_title=F('level__title'),
                author_username=F('level__author__username'),
                author_email=F('level__author__email'),
                price=F('level__price'),
            )
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

