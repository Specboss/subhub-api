import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView

from .tasks import telegram_webhook_task
from .auth_telegram import TelegramAuth

@csrf_exempt
def telegram_webhook(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)
    try:
        data = json.loads(request.body) if request.body else {}
    except (json.JSONDecodeError, ValueError) as e:
        return JsonResponse({"ok": True})
    message = data.get("message") or data.get("edited_message")
    if not message:
        return JsonResponse({"ok": True})
    chat_id = message["chat"]["id"]
    text = message.get("text", "")
    telegram_webhook_task.delay(chat_id, text)
    return JsonResponse({"ok": True})

class TelegramAuthApiView(GenericAPIView):

    def post(self, request, *args, **kwargs):


