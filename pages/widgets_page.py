import time

from selenium.webdriver import Keys

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


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

    def check_multi_input(self):
        input = self.element_is_visible(self.locators.MULTI_INPUT)
        colors = ["Red", "Yellow", "Green"]
        for color in colors:
            input.send_keys(color)
            input.send_keys(Keys.RETURN)
        return colors

    def get_actual_colors(self):
        input_values = self.elements_are_present(self.locators.MULTI_VALUE)
        actual_colors = [i.text for i in input_values]
        return actual_colors

    def remove_colors(self):
        remove_btns = self.elements_are_visible(self.locators.REMOVE_VALUE)
        for i in range(2):
            remove_btns[i].click()