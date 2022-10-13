# импортируем функцию создания объекта бота
from telebot import TeleBot
# импортируем основные настройки проекта
from settings import config
# импортируем главный класс-обработчик бота
from handlers.handler_main import HandlerMain
# импортируем классс для запуска браузера и переключения к фрейму с расписанием



class TelBot:
    """
    Основной класс телеграмм бота (сервер), в основе которого
    используется библиотека pyTelegramBotAPI
    """
    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        """
        Инициализация бота
        """
        # получаем токен
        self.token = config.TOKEN
        # инициализируем бот на основе зарегистрированного токена
        self.bot = TeleBot(self.token)
        # инициализируем оброботчик событий
        self.handler = HandlerMain(self.bot)



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




if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()




#active_frame = FrameSwitcher(TEACHER_LINK, XPATH)
#active_frame.start_browser()
#get_driver = active_frame.get_start_browser()

#actual_teacher_list = ParserTeachersList(XPATH_NAME_INPUT_FIELD, TEACHERS_LIST_HTML, get_driver)
#actual_teacher_list.get_teacher_list()