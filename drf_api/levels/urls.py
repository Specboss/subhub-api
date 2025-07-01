from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('author/<int:author_id>/levels/', views.ListLevelsAPIView.as_view(), name='levels-author-list'),
    path('subscribtions/', LevelUserApiView.as_view(), name=''),

]
router = DefaultRouter()
router.register(r'levels', views.LevelsViewSet, basename='levels')
router.register(r'subscribers', views.AuthorSubscribersViewSet, basename='author-subscribers')
urlpatterns += router.urls