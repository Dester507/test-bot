from telegram.ext import Dispatcher, CommandHandler

from .handlers import start_command


def create_dispatcher(disp: Dispatcher) -> Dispatcher:
    # Adding handlers for events
    disp.add_handler(CommandHandler("start", start_command))
    return disp
