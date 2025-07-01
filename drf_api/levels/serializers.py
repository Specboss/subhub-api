from rest_framework import serializers

from app.levels.models import Level


class LevelSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Level
        fields = '__all__'