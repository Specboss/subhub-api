from rest_framework_simplejwt.tokens import RefreshToken

from app.users.models import User

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