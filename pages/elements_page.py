import time

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxLocators, RadioButtonLocators
from pages.base_page import BasePage
import random


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    """Заполнение всех полей и подтверждение"""
    def fill_all_fields(self):
        # при каждом вызове next т.е. person_info получаем следующий элемент списка
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_adress = person_info.current_adress
        permanent_adress = person_info.permanent_adress
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys(current_adress)
        self.element_is_visible(self.locators.PERMANENT_ADRESS).send_keys(permanent_adress)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        # возвращаем значения которые заполняли для проверки
        return full_name, email, current_adress, permanent_adress

    """Проверяем отображаемые после заполнения поля"""
    def check_field_form(self):
        """Получаем текст каждого элемента и обрезаем его ключ, возвращаем только значение"""
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_present(self.locators.CREATED_CURRENT_ADRESS).text.split(':')[1]
        permanent_adress = self.element_is_present(self.locators.CREATED_PERMANENT_ADRESS).text.split(':')[1]
        return full_name, email, current_adress, permanent_adress

class CheckBoxPage(BasePage):

    locators = CheckBoxLocators()
    """Открыть список чекбоксов"""
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()
    """Кликнуть по случайном чекбоксу"""
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 10
        while count != 0:
            item = item_list[random.randint(1,15)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def click_all_checkbox(self):
        """Получаем список элементов и кликаем по каждому"""
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        for item in item_list:
            self.go_to_element(item)
            item.click()

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            """В каждом чекбоксе списка находим title, * перед локатором нужна для распаковки аргументов т.к. find
            element принимает их как строку"""
            item_title = box.find_element(*self.locators.ITEM_TITLE)
            """Добавляем текст заголовком в список"""
            data.append(item_title.text)
        """Возвращаем список как строку приведённую в общий вид с output строкой"""
        return str(data).lower().replace(".doc", "").replace(" ", "")

    def get_output_results(self):
        """Получаем текст output элементов, убираем лишние пробелы(зачем в файле debug)"""
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULTS)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(" ", "")

class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_on_radio_button(self, choice):
        """Создаём словарь с ключом в виде заголовка радио, присваиваем им селекторы"""
        choices = {
            "yes": self.locators.YES_RADIOBUTTON,
            "impressive": self.locators.IMPRESSIVE_RADIOBUTTON,
            "no": self.locators.NO_RADIOBUTTON,
        }
        """Проверяем видимость и кликаем, choice передаём через аргумент функции"""
        self.element_is_visible(choices[choice]).click()

    def get_checked_radio_titles(self):
        """При выборе радио может отображаться только текст выбранного, поэтому получаем его"""
        return self.element_is_present(self.locators.OUTPUT_RESULT).text






