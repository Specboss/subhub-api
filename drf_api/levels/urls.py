from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('<int:author_id>/levels/', views.ListLevelsAPIView.as_view(), name='levels-author-list'),
    #path('level-user/', LevelUserApiView.as_view(), name='level-user-api'),
]

router = DefaultRouter()
router.register(r'levels', views.LevelsViewSet, basename='levels')
urlpatterns += router.urls