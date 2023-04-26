from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


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
