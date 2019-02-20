from telegram.ext import CommandHandler

from ..handlers import HandlerInterface


class Rules(HandlerInterface):
    """ Test echo command for bot"""
    handler = CommandHandler

    def apply(self, bot, update):
        update.message.reply_text("Придерживаемся правил сообщества\nhttps://t.me/pydjango/153321")
