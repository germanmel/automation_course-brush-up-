import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators
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

class DataPickerPage(BasePage):
    locators = DataPickerPageLocators()

    def fill_random_month(self):
        """Кликаем поле чтобы открыть пикер"""
        date_field = self.element_is_visible(self.locators.DATE_INPUT).click()
        """Находим дропдаун"""
        dropdown_months = self.element_is_visible(self.locators.DATE_SELECT_MONTH)
        """Генерируем список месяцев"""
        months_list = [i.text for i in dropdown_months.find_elements(By.TAG_NAME, 'option')]
        print(months_list)
        """Выбираем любой месяц из списка"""
        month = months_list[random.randint(0, len(months_list)-1)]
        print(month)
        dropdown_months.send_keys(month)
        month_num = months_list.index(month) + 1
        if month_num < 10:
            return f"0{month_num}"
        else:
            return month_num

    def fill_random_year(self):
        date_field = self.element_is_visible(self.locators.DATE_INPUT).click()
        dropdown_years = self.element_is_visible(self.locators.DATE_SELECT_YEAR)
        years_list = [i.text for i in dropdown_years.find_elements(By.TAG_NAME, 'option')]
        year = years_list[random.randint(0, len(years_list)-1)]
        dropdown_years.send_keys(year)
        return year

    def fill_random_day(self):
        date_field = self.element_is_visible(self.locators.DATE_INPUT).click()
        """Тут дивы вместо дропдауна, поэтому берём все элементы класса"""
        elements = self.elements_are_visible(self.locators.DATE_SELECT_DAY_LIST)
        """Выбираем один из элементов"""
        day_element = elements[random.randint(0, len(elements)-1)]
        """Сначала получаем текст, потом кликаем, если наоборот элемента не будет в дереве и ошибка"""
        day_text = day_element.text
        day_element.click()
        if int(day_text) < 10:
            return f"0{day_text}"
        else:
            return day_text

    def get_entered_date(self):
        date_field = self.element_is_visible(self.locators.DATE_INPUT)
        actual_date = date_field.get_attribute("value")
        return actual_date

    def fill_datetime_month(self):
        date_field = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).click()
        """Чтобы появились элементы нужно кликнуть по списку"""
        dropdown_months = self.element_is_visible(self.locators.DATE_AND_TIME_MONTH_SELECT).click()
        elements = self.elements_are_visible(self.locators.DATE_AND_TIME_MONTH_LIST)
        """Выбираем один из элементов"""
        month_element = elements[random.randint(0, len(elements) - 1)]
        month_name = month_element.text
        month_element.click()
        return month_name

    def fill_datetime_day(self):
        date_field = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).click()
        """Тут дивы вместо дропдауна, поэтому берём все элементы класса"""
        elements = self.elements_are_visible(self.locators.DATE_AND_TIME_SELECT_DAY_LIST)
        """Выбираем один из элементов"""
        day_element = elements[random.randint(0, len(elements) - 1)]
        """Сначала получаем текст, потом кликаем, если наоборот элемента не будет в дереве и ошибка"""
        day_text = day_element.text
        day_element.click()
        return day_text

    def fill_datetime_year(self):
        date_field = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).click()
        dropdown_year = self.element_is_visible(self.locators.DATE_AND_TIME_YEAR_SELECT).click()
        elements = self.elements_are_visible(self.locators.DATE_AND_TIME_YEAR_LIST)
        """Выбираем один из элементов"""
        year_element = elements[random.randint(0, len(elements) - 1)]
        """Сначала получаем текст, потом кликаем, если наоборот элемента не будет в дереве и ошибка"""
        year_text = year_element.text
        year_element.click()
        return year_text

    def fill_datetime_time(self):
        date_field = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).click()
        elements = self.elements_are_visible(self.locators.DATE_AND_TIME_SELECT_TIME)
        time_element = elements[random.randint(0, len(elements) - 1)]
        time_text = time_element.text
        time_element.click()
        return time_text


    def get_entered_timedate(self):
        date_field = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        actual_date = date_field.get_attribute("value")
        return actual_date
