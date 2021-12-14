from django.conf import settings
from telegram import Bot
from telegram.ext import (
    Updater
)

from .dispatcher import create_dispatcher


def start_pooling():
    # Run bot
    updater = Updater(settings.BOT_TOKEN)
    disp = create_dispatcher(updater.dispatcher)
    bot = Bot(settings.BOT_TOKEN).get_me()
    print(f'Bot link without referral_id -> https://t.me/{bot["username"]}')
    print(f'Bot link with referral_id -> https://t.me/{bot["username"]}?start=12367507')
    updater.start_polling()
    updater.idle()
