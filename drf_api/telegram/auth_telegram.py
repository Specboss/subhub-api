import hashlib
import hmac
from urllib.parse import parse_qsl
from rest_framework_simplejwt.tokens import RefreshToken

from app.users.models import User

def verify_telegram_init_data(init_data: str, bot_token: str) -> dict:
    data = dict(parse_qsl(init_data, strict_parsing=True))
    hash_ = data.pop("hash", None)
    if not hash_:
        raise ValueError("hash not found")

    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
    secret_key = hashlib.sha256(bot_token.encode()).digest()
    calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
    if calculated_hash != hash_:
        raise ValueError("Invalid initData hash")

    return data

class TelegramAuth:
    def __init__(self, init_data):
        self.telegram_id = int(init_data["user[id]"])
        self.username = init_data.get("user[username]", "")
        self.first_name = init_data.get("user[first_name]", "")
        self.last_name = init_data.get("user[last_name]", "")
        self.user = None
        self.created = None

    def execute(self):
        self.user, self.created = User.objects.get_or_create(
            tg_user_id=self.telegram_id,
            defaults={
                "email": f"{self.telegram_id}@telegram.local",
                "username": self.username or f"tg_{self.telegram_id}",
                "first_name": self.first_name,
                "last_name": self.last_name,
                "tg_username": self.username,
                "tg_first_name": self.first_name,
                "tg_last_name": self.last_name,
                "password": User.objects.make_random_password()
            }
        )

    def get_token(self):
        return RefreshToken.for_user(self.user)
