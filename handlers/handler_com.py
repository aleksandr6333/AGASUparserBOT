# импортируем класс родитель
from handlers.handler import Handler


class HandlerCommands(Handler):
    """
    Класс обрабатывает входящие команды /start и /help и т.п.
    """
    def __init__(self, bot, TEACHERS_LIST_HTML, get_driver):
        super().__init__(bot, TEACHERS_LIST_HTML, get_driver)

        self.teacher_list = TEACHERS_LIST_HTML
        self.get_driver = get_driver  # Переменная driver полученная через геттер от класса FrameSwitcher

    def pressed_btn_start(self, message):
        """
        обрабатывает входящие /start команды
        """
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' здравствуйте! Жду дальнейших задач.',
                              reply_markup=self.keybords.start_menu())

    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие /start команды.
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(type(message))
            if message.text == '/start':
                self.pressed_btn_start(message)
