from locators.element_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    """Заполнение всех полей и подтверждение"""
    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Python")
        self.element_is_visible(self.locators.EMAIL).send_keys("python@mail.ru")
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys("Moscow")
        self.element_is_visible(self.locators.PERMANENT_ADRESS).send_keys("Rostov")
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    """Проверяем отображаемые после заполнения поля"""
    def check_field_form(self):
        """Получаем текст каждого элемента и обрезаем его ключ, возвращаем только значение"""
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_present(self.locators.CREATED_CURRENT_ADRESS).text.split(':')[1]
        permanent_adress = self.element_is_present(self.locators.CREATED_PERMANENT_ADRESS).text.split(':')[1]
        return full_name, email, current_adress, permanent_adress


