from rest_framework import serializers
import hashlib
import hmac
import json
import os

from app.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "second_name", "email",
            "tg_user_id", "tg_username", "tg_first_name", "tg_last_name"
        ]
        read_only_fields = ["id", "tg_user_id", "tg_username", "tg_first_name", "tg_last_name"]

    # def validate(self, attrs):
    #     """
    #     Проверка подписи hash из Telegram initData
    #     """
    #     user_data = attrs.get('user')
    #
    #     # Собираем строку для HMAC
    #     data_check_string = "\n".join([
    #         f"auth_date={attrs['auth_date']}",
    #         f"query_id={attrs['query_id']}",
    #         f"user={self._serialize_user(user_data)}"
    #     ])
    #
    #     # Генерируем HMAC-SHA256
    #     secret_key = hashlib.sha256(os.getenv('TELEGRAM_BOT_TOKEN').encode()).digest()
    #     hmac_hash = hmac.new(secret_key, msg=data_check_string.encode(), digestmod=hashlib.sha256).hexdigest()
    #
    #     if hmac_hash != attrs.get('hash'):
    #         raise serializers.ValidationError("Некорректная подпись Telegram (hash mismatch)")
    #
    #     return attrs
    #
    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     tg_user_id = user_data['id']
    #
    #     user, _ = User.objects.update_or_create(
    #         tg_user_id=tg_user_id,
    #         defaults={
    #             "tg_username": user_data.get("username"),
    #             "tg_first_name": user_data.get("first_name"),
    #             "tg_last_name": user_data.get("last_name"),
    #             "first_name": user_data.get("first_name"),
    #             "last_name": user_data.get("last_name"),
    #             "user_type": validated_data.get("user_type")
    #         }
    #     )
    #     return user
    #
    # def _serialize_user(self, user_dict):
    #     # Telegram сериализует user как JSON без пробелов
    #     return json.dumps(user_dict, separators=(',', ':'))