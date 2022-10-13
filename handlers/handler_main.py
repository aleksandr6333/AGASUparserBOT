# импортируем класс HandlerCommands обработка комманд
from handlers.handler_com import HandlerCommands


class HandlerMain:
    """
    Класс-компоновщик
    """
    def __init__(self, bot):
        # получаем объект нашего бота
        self.bot = bot
        # здесь будет инициализация обработчиков
        self.handler_commands = HandlerCommands(self.bot)

    def handle(self):
        # здесь будет запуск обработчиков
        self.handler_commands.handle()
