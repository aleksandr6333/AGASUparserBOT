# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
# импортируем настройки и утилиты
from settings import config
# импортируем класс-менеджер для работы с библиотекой
# data_base.dbalchemy import DBManager
# импортируем парсер собирающий список преподавателей

from parserr.parser_teachers_list import ParserTeachersList
from parserr.frame_switcher import FrameSwitcher
from settings.config import TEACHERS_LIST_HTML

class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """
    # инициализация разметки

    def __init__(self, TEACHERS_LIST_HTML, get_driver):
        self.markup = None
        # инициализируем менеджер для работы с БД
        #self.BD = DBManager()
        self.teacher_list = TEACHERS_LIST_HTML
        self.get_driver = get_driver  # Переменная driver полученная через геттер от класса FrameSwitcher
        self.parser_teacher_list = ParserTeachersList(self, TEACHERS_LIST_HTML, get_driver)

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """

        return KeyboardButton(config.KEYBOARD[name])

#    def start_menu(self):
#        """
#        Создает разметку кнопок в основном меню и возвращает разметку
#        """
#        self.markup = ReplyKeyboardMarkup(True, True)
#        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
#        itm_btn_2 = self.set_btn('INFO')
#        itm_btn_3 = self.set_btn('SETTINGS')
#        # рассположение кнопок в меню
#        self.markup.row(itm_btn_1)
#        self.markup.row(itm_btn_2, itm_btn_3)
#        return self.markup
    def start_menu(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)

        buttons = self.parser_teacher_list.get_teacher_list()
        for button in buttons:
            itm_btn = self.set_btn(button)

            # рассположение кнопок в меню
            self.markup.row(itm_btn)
            return self.markup
