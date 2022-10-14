# импортируем функцию создания объекта бота
from telebot import TeleBot
# импортируем основные настройки проекта
from settings import config
# импортируем главный класс-обработчик бота
from handlers.handler_main import HandlerMain
# импортируем классс для запуска браузера и переключения к фрейму с расписанием
from parserr.start_parsing import StartParsing

from settings.config import XPATH, TEACHER_LINK

class TelBot:
    """
    Основной класс телеграмм бота (сервер), в основе которого
    используется библиотека pyTelegramBotAPI
    """
    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self, TEACHER_LINK, XPATH):
        """
        Инициализация бота
        """
        # получаем токен
        self.token = config.TOKEN
        # инициализируем бот на основе зарегистрированного токена
        self.bot = TeleBot(self.token)
        # инициализируем оброботчик событий
        self.handler = HandlerMain(self.bot)

        self.teacher_link = TEACHER_LINK
        self.xpath = XPATH
        self.start_parser = StartParsing(self.bot, XPATH)


    def start(self):
        """
        Метод предназначен для старта обработчика событий
        """
        self.handler.handle()

    def run_bot(self):
        """
        Метод запускает основные события сервера
        """
        # обработчик событий
        self.start()
        # служит для запуска бота (работа в режиме нон-стоп)
        self.bot.polling(none_stop=True)

    def start_parser(self):
        self.start_parser.start_parsing()


if __name__ == '__main__':
    bot = TelBot(TEACHER_LINK, XPATH)
    bot.run_bot()
    bot.start_parser()




#active_frame = FrameSwitcher(TEACHER_LINK, XPATH)
#active_frame.start_browser()
#get_driver = active_frame.get_start_browser()

#actual_teacher_list = ParserTeachersList(XPATH_NAME_INPUT_FIELD, TEACHERS_LIST_HTML, get_driver)
#actual_teacher_list.get_teacher_list()