import os

import yaml
from telegram.ext import Updater

from .exceptions import TelegramTokenException
from . import modules


class HelpBot(object):
    updater = None
    config = None

    def __init__(self, cfg):
        token = os.getenv('TELEGRAM_TOKEN')
        if not token:
            raise TelegramTokenException()
        self.updater = Updater(token)
        with open(cfg, 'r') as stream:
            self.config = yaml.load(stream)

    def _load_modules(self):
        for module in self.config.get('modules', []):
            self._load_module(module)

    def _load_module(self, module_name):
        module = getattr(modules, module_name)(**self.config.get(module_name, {}))
        self.updater.dispatcher.add_handler(module.handle())

    def run(self):
        self._load_modules()
        return self.updater.start_polling()
