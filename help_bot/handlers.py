class HandlerInterface(object):
    handler = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def apply(self, bot, update):
        raise NotImplementedError

    def handle(self):
        return self.handler(self.__class__.__name__.lower(), self.__getattribute__('apply'))
