import django_filters

from app.post_feedbacks import models as feedback_models
from app.posts.models import Post


class PostFilter(django_filters.FilterSet):
    author = django_filters.NumberFilter(field_name='level__author__id')
    is_pin = django_filters.BooleanFilter()
    is_ads = django_filters.BooleanFilter()
    currency = django_filters.CharFilter()

    class Meta:
        model = Post
        fields = ['author', 'is_pin', 'is_ads', 'currency']