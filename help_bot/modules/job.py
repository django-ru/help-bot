from telegram.ext import CommandHandler

from ..handlers import HandlerInterface


class Job(HandlerInterface):
    """ Test echo command for bot"""
    handler = CommandHandler

    def apply(self, bot, update):
        update.message.reply_text("@django_jobs - чат для размещения вакансий и резюме связанные с Django\n"
                                  "@python_jobs - чат для размещения вакансий и резюме связанные с Python")
