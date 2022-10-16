from selenium.webdriver.common.by import By


class ParserTeachersList:
    def __init__(self, XPATH_NAME_INPUT_FIELD, TEACHERS_LIST_HTML, get_driver):
        self.xpath_name_input_field = XPATH_NAME_INPUT_FIELD
        self.teachers_list_html = TEACHERS_LIST_HTML
        self.get_driver = get_driver # Переменная driver полученная через геттер от класса FrameSwitcher

    def get_teacher_list(self):
        self.name_all_teachers = self.get_driver.find_element(By.XPATH, self.xpath_name_input_field).click()
        self.search_for_list_teacher = self.get_driver.find_element(By.XPATH, self.teachers_list_html)
        self.teachers_list = self.search_for_list_teacher.find_element(By.XPATH, self.teachers_list_html)
        self.teachers = self.teachers_list.find_elements(By.TAG_NAME, 'li')
        self.teacher = {teacher.text for teacher in self.teachers}  # Получаем всех преподавателей списком через генератор списков в этой строке
        return self.teacher
       #print(self.teacher)