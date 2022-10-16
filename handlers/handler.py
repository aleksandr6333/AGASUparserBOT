# импортируем библиотеку abc для реализации абстрактных классов
import abc
# импортируем разметку клавиатуры и клавиш
from markup.markup import Keyboards
# импортируем класс-менеджер для работы с библиотекой
#from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot, TEACHERS_LIST_HTML, get_driver):
        # получаем объект бота
        self.bot = bot

        self.teacher_list = TEACHERS_LIST_HTML
        self.get_driver = get_driver  # Переменная driver полученная через геттер от класса FrameSwitcher
        # инициализируем разметку кнопок
        self.keybords = Keyboards(TEACHERS_LIST_HTML, get_driver)
        # инициализируем менеджер для работы с БД
        #self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
