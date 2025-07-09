from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'posts', views.PostsViewSet)
router.register(r'post-likes', views.PostLikeViewSet)
router.register(r'comments',views.CommentViewSet)
router.register(r'comment-reactions', views.CommentReactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]