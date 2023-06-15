import os
import time

from selenium.webdriver import Keys

from selenium.webdriver.support.select import Select
from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    def fill_form(self):
        person_info = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person_info.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person_info.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person_info.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person_info.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys("Chemistry")
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person_info.current_adress)
        """Cначала кликаем на селектор, затем в инпут отправляем текст"""
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys("Haryana")
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys("Karnal")
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person_info


    def form_resul(self):
        """Получаем список из правой части таблицы, проходим по каждому элементу и сохраняем его текст"""
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data







    def check_filled_form(self):
        pass