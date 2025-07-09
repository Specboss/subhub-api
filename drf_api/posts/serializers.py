from rest_framework import serializers

from app.post_feedbacks import models as post_feedback_models
from app.posts.models import Post
from app.attachments.models import Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'file', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = [
            'id', 'level', 'title', 'description', 'can_comment', 'is_ads',
            'support_amount', 'currency', 'is_pin', 'created_at', 'updated_at',
            'attachments'
        ]

    def create(self, validated_data):
        attachments_data = validated_data.pop('attachments', [])
        post = Post.objects.create(**validated_data)
        for attachment_data in attachments_data:
            Attachment.objects.create(post=post, **attachment_data)
        return post

    def update(self, instance, validated_data):
        attachments_data = validated_data.pop('attachments', [])
        # Обновляем пост
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Можно добавить логику обновления вложений,
        # например, удалить старые и добавить новые или обновлять по id
        # Для простоты здесь добавим только новые:
        for attachment_data in attachments_data:
            Attachment.objects.create(post=instance, **attachment_data)

        return instance

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_feedback_models.PostLike
        fields = '__all__'
        read_only_fields = ('created_at',)

class CommentSerializer(serializers.ModelSerializer):
    reactions_count = serializers.IntegerField(source='reactions.count', read_only=True)

    class Meta:
        model = post_feedback_models.Comment
        fields = '__all__'
        read_only_fields = ('created_at',)

class CommentReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_feedback_models.CommentReaction
        fields = '__all__'
        read_only_fields = ('created_at',)