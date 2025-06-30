from enum import Enum

class TelegramMessagesEnum(Enum):
    UNKNOWN_COMMAND = "❌ Команда не поддерживается."
    GREETING = (
        "Привет! 🎉 Добро пожаловать в SUPLO — удобный сервис для переводов крипты в TON через Telegram! 🚀\n\n"
        "Вот что мы предлагаем:\n"
        "✅ Быстрые и безопасные транзакции\n"
        "✅ Простота использования\n"
        "✅ Поддержка на каждом шаге"
    )
