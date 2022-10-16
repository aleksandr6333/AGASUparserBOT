# импортируем класс HandlerCommands обработка комманд
from handlers.handler_com import HandlerCommands


class HandlerMain:
    """
    Класс-компоновщик
    """
    def __init__(self, bot, TEACHERS_LIST_HTML, get_driver):
        # получаем объект нашего бота
        self.bot = bot
        # здесь будет инициализация обработчиков
        self.handler_commands = HandlerCommands(self.bot, TEACHERS_LIST_HTML, get_driver)

        self.teacher_list = TEACHERS_LIST_HTML
        self.get_driver = get_driver  # Переменная driver полученная через геттер от класса FrameSwitcher
    def handle(self):
        # здесь будет запуск обработчиков
        self.handler_commands.handle()
