from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings.config import TEACHER_LINK, XPATH

driver = webdriver.Chrome() # Через драйвер подключаем использование браузера Chrome
# Указываем адрес страницы для автоматизации
driver.get(TEACHER_LINK)

iframe = driver.find_element(By.XPATH, XPATH) # Поиск фрейма по указанному пути
driver.switch_to.frame(iframe) # Переключение на найденный фрейм с расписанием


# Выбор значения из дропсписка "Период"
xpath_week = '/html/body/div/div/div[1]/div/form/div[1]/div/div/div[1]' # Путь к дропсписку "Период"
week = driver.find_element(By.XPATH, xpath_week).click() # Поиск дропсписка с указанием недель

now_week_xpath = '/html/body/div/div/div[1]/div/form/div[1]/div/div/div[2]/ul[2]/li[1]' # Путь к значению дроп списка "текущая неделя"
now_week = driver.find_element(By.XPATH, now_week_xpath).click() # Поиск и выбор значения из дропсписка "текущая неделя"

#next_week_xpath = '/html/body/div/div/div[1]/div/form/div[1]/div/div/div[2]/ul[2]/li[2]' # Путь к значению дроп списка "следующая неделя"
#next_week = driver.find_element(By.XPATH, next_week_xpath).click() # Поиск и выбор значения из дропсписка "следующая неделя"

#now_next_week_xpath = '/html/body/div/div/div[1]/div/form/div[1]/div/div/div[2]/ul[2]/li[3]' # Путь к значению дроп списка "текущая и следующая неделя"
#now_next_week = driver.find_element(By.XPATH, now_next_week_xpath).click() # Поиск и выбор значения из дропсписка "текущая и следующая неделя"

#period_xpath = '/html/body/div/div/div[1]/div/form/div[1]/div/div/div[2]/ul[2]/li[4]' # Путь к значению дроп списка "заданный период"
#period_week = driver.find_element(By.XPATH, period_xpath).click() # Поиск и выбор значения из дропсписка "заданный период"

# Выбор значения из дропсписка "Учреждение"
xpath_educational_institution = '/html/body/div/div/div[1]/div/form/div[2]/div/div/div[1]' # Путь к дропсписку "Учреждение"
educational_institution = driver.find_element(By.XPATH, xpath_educational_institution).click() # Поиск дропсписка с указанием учебных заведений

xpath_educational_institution_agasu = '/html/body/div/div/div[1]/div/form/div[2]/div/div/div[2]/ul[2]/li[1]' # Путь к значению дроп списка "АГАСУ"
educational_institution_agasu = driver.find_element(By.XPATH, xpath_educational_institution_agasu).click() # Поиск и выбор значения из дропсписка "АГАСУ"

#xpath_educational_institution_construction_college = '/html/body/div/div/div[1]/div/form/div[2]/div/div/div[2]/ul[2]/li[2]' # Путь к значению
#дропсписка "Строительный колледж"
#educational_institution_construction_college= driver.find_element(By.XPATH, xpath_educational_institution_construction_college).click() # Поиск
#и выбор значения из дропсписка "Строительный колледж"

#xpath_educational_institution_gkh_college = '/html/body/div/div/div[1]/div/form/div[2]/div/div/div[2]/ul[2]/li[3]' # Путь к значению дропсписка "ЖКХ колледж"
#educational_institution_gkh_college= driver.find_element(By.XPATH, xpath_educational_institution_gkh_college).click() # Поиск и выбор значения из дропсписка "ЖКХ колледж"

#xpath_educational_institution_agasu_asp = '/html/body/div/div/div[1]/div/form/div[2]/div/div/div[2]/ul[2]/li[4]' # Путь к значению дроп списка "АГАСУ(асп)"
#educational_institution_agasu_asp = driver.find_element(By.XPATH, xpath_educational_institution_agasu_asp).click() # Поиск и выбор значения из дропсписка "АГАСУ(асп)"

#xpath_educational_institution_agasu_pu = '/html/body/div/div/div[1]/div/form/div[2]/div/div/div[2]/ul[2]/li[5]' # Путь к значению дроп списка "ПУ АГАСУ"
#educational_institution_agasu_pu = driver.find_element(By.XPATH, xpath_educational_institution_agasu_pu).click() # Поиск и выбор значения из дропсписка "ПУ АГАСУ"

#xpath_educational_institution_agasu_pdg = '/html/body/div/div/div[1]/div/form/div[2]/div/div/div[2]/ul[2]/li[6]' # Путь к значению дроп списка "АГАСУ(пдг)"
#educational_institution_agasu_pdg = driver.find_element(By.XPATH, xpath_educational_institution_agasu_pdg).click() # Поиск и выбор значения из дропсписка "АГАСУ(пдг)"




# Выбор значения из дропсписка "Преподаватель"
xpath_teacher_droplist = '/html/body/div/div/div[1]/div/form/div[3]/div/div/div[1]' # Путь к дропсписку "Преподаватель"
teacher_droplist = driver.find_element(By.XPATH, xpath_teacher_droplist).click() # Поиск дропсписка с указанием преподавателей

#Ввод части фамилии для поиска
xpath_name_input_field = '/html/body/div/div/div[1]/div/form/div[3]/div/div/div[1]/div/input' # Путь к полю ввода
name_input_field = driver.find_element(By.XPATH, xpath_name_input_field).send_keys("олейников" + Keys.DOWN  + Keys.ENTER) # Поиск поля ввода текста и ввод
# Вместо олейников input или событие от кнопки





#Парсим список преподов и передаем в список, потом перебираем в цикле и привязываем к кнопкам с событиями в боте
xpath_name_input_field = '/html/body/div/div/div[1]/div/form/div[3]/div/div/div[1]/div/input'
# Путь к полю ввода
name_all_teachers = driver.find_element(By.XPATH, xpath_name_input_field).click()
# Поиск поля ввода текста, передача одного пробела для получения всего списка преподавателей


teachers_list_html = '/html/body/div/div/div[1]/div/form/div[3]/div/div/div[2]/ul[2]'

search_for_list_teacher = driver.find_element(By.XPATH, teachers_list_html)

teachers_list = search_for_list_teacher.find_element(By.XPATH, teachers_list_html)
teachers = teachers_list.find_elements(By.TAG_NAME, 'li')

#for prepod in prepods:
#    text = prepod.text
#    print (text)


teacher = [teacher.text for teacher in teachers] # Получаем всех преподавателей списком через генератор списков в этой строке
print(teacher)












