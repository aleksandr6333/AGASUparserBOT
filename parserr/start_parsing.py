from parserr.frame_switcher import FrameSwitcher
from parserr.parser_teachers_list import ParserTeachersList
from settings.config import XPATH_NAME_INPUT_FIELD, TEACHERS_LIST_HTML, XPATH, TEACHER_LINK



class StartParsing:
    def __init__(self, TEACHER_LINK, XPATH):
        self.teacher_link = TEACHER_LINK
        self.xpath = XPATH
        self.xpath_name_input_field = XPATH_NAME_INPUT_FIELD
        self.teachers_list_html = TEACHERS_LIST_HTML


    def start_parsing(self):
        active_frame = FrameSwitcher(TEACHER_LINK, XPATH)
        active_frame.start_browser()
        get_driver = active_frame.get_start_browser()
        actual_teacher_list = ParserTeachersList(XPATH_NAME_INPUT_FIELD, TEACHERS_LIST_HTML, get_driver)
        actual_teacher_list.get_teacher_list()
        return get_driver
        #print ("OKК")