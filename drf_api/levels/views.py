from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets

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

class ListLevelsAPIView(ListAPIView):
    serializer_class = serializers.LevelSerializer
    permission_classes = [IsAuthenticated, auth_permission.User]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['price']
    ordering = ['price']

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        return Level.objects.filter(author_id=author_id)

class AuthorSubscribersAPIView(ListAPIView):
    pagination_class = InfinitePagination
    permission_classes = [auth_permission.Author]
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