import time

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage
import random



class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        #Для удобства создаём словарь и присваивам номеру секции локатор заголовка и контента
        accordian = {1:
                         {"title": self.locators.SECTION_1,
                          "content": self.locators.SECTION_1_CONTENT},
                     2:
                         {"title": self.locators.SECTION_2,
                          "content": self.locators.SECTION_2_CONTENT},
                     3:
                         {"title": self.locators.SECTION_3,
                          "content": self.locators.SECTION_3_CONTENT},
                     }
        section_title = self.element_is_present(accordian[accordian_num]["title"])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]["content"]).text
        return section_title.text, section_content

class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    """Добавляем все цвета из списка в инпут и возвращаем этот список"""
    def check_multi_input(self):
        input = self.element_is_visible(self.locators.MULTI_INPUT)
        """"random.sample выбирает случайные элементы в количестве k=x"""
        colors = random.sample(next(generated_color()).color_name, k=6)
        for color in colors:
            input.send_keys(color)
            input.send_keys(Keys.RETURN)
        return colors

    """Если в инпуте пустота - возвращаем False, иначе возвращаем список значений"""
    def get_actual_colors(self):
        input_values = self.elements_are_present(self.locators.MULTI_VALUE)
        if input_values != False:
            actual_colors = [i.text for i in input_values]
            return actual_colors
        else:
            return False

    """Удаляем все значения из инпута поочерёдно"""
    def remove_colors(self):
        remove_btns = self.elements_are_visible(self.locators.REMOVE_VALUE)
        for btn in remove_btns:
            btn.click()
    """Удаляем все значения инпута по кнопке удалить все(крестик)"""
    def remove_all_colors(self):
        remove_all_btn = self.element_is_visible(self.locators.REMOVE_ALL_VALUE).click()

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_INPUT_VALUE)
        return color.text