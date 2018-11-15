class TelegramTokenException(Exception):
    def __init__(self):
        super().__init__('Your environment vars must set "TELEGRAM_TOKEN" variable for bot')
