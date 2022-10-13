from selenium import webdriver
from selenium.webdriver.common.by import By
from settings.config import TEACHER_LINK, XPATH


class FrameSwitcher:
    def __init__(self, TEACHER_LINK, XPATH):
        self.teacher_link = TEACHER_LINK
        self.xpath = XPATH

    def start_browser(self):
        self.driver = webdriver.Chrome() # Через драйвер подключаем использование браузера Chrome
        self.teacher_link = self.driver.get(self.teacher_link) # Указываем адрес страницы для автоматизации
        self.iframe = self.driver.find_element(By.XPATH, self.xpath) # Поиск фрейма по указанному пути
        self.driver.switch_to.frame(self.iframe) # Переключение на найденный фрейм с расписанием
        print ("OK")

    def get_start_browser(self): # геттер возвращающий переменную driver для класса ParserTeachersList
        return self.driver