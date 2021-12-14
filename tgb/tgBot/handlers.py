from telegram import Update
from telegram.ext import CallbackContext

from .models import Profile


# /start command
def start_command(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 1 and context.args[0].isnumeric():
        try:
            user_profile = Profile.objects.get(referral_id=context.args[0])
            msg = f"Приветствую {user_profile.user_name}! Твой уникальный код - {user_profile.user_id}"
        except Profile.DoesNotExist:
            msg = "Неверный реферальный код"
    else:
        msg = "Вы не можете начать использовать бот без реферальной ссылки. " \
              "Перейдите в бот с помощью реферальной ссылки"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
