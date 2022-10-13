import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = ''
# название БД
#NAME_DB = 'products.sqlite'
# версия приложения
VERSION = '0.1'
# автор приложния
AUTHOR = 'User'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
#DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

#COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    #'AMOUNT_PRODUCT': COUNT,
    #'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
#CATEGORY = {
#    'SEMIPRODUCT': 1,
#    'GROCERY': 2,
#    'ICE_CREAM': 3,
#}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}

# Путь к странице с расписанием преподавателей
TEACHER_LINK = 'https://xn--80aai1dk.xn--p1ai/studentam/raspisanie-zanyatij-prepodavatelej'
# Путь к фрейму на странице, так как расписание формируется динамически через js
XPATH = '/html/body/div[1]/section/section[3]/div/div/div[2]/p/iframe'
# Путь к полю ввода "Преподаватель"
XPATH_NAME_INPUT_FIELD = '/html/body/div/div/div[1]/div/form/div[3]/div/div/div[1]/div/input'
# Путь к списку преподавателей (формируется после активации фрейма !???)
TEACHERS_LIST_HTML = '/html/body/div/div/div[1]/div/form/div[3]/div/div/div[2]/ul[2]'