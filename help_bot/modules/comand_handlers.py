from telegram.ext import CommandHandler

from ..handlers import HandlerInterface


class Hello(HandlerInterface):
    """ Test echo command for bot"""
    handler = CommandHandler

    def apply(self, bot, update):
        update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))
