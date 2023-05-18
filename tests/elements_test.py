import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
from random import randint


class TestTextBox:

    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        #  Получаем переменные из return функций по проверке заполнения и заполненных полей
        full_name, email, current_adress, permanent_adress = text_box_page.fill_all_fields()
        output_name, output_email, output_cur_adress, output_per_adress = text_box_page.check_field_form()
        assert full_name == output_name, f"Full name {full_name} differs from output name {output_name}"
        assert email == output_email, f"Email {email} differs from output email {output_email}"
        assert current_adress == output_cur_adress, \
            f'Current adress {current_adress} differs from output cur adress {output_cur_adress}'
        assert permanent_adress == output_per_adress, \
            f"Permanent adress {permanent_adress} differs from output per adress {output_per_adress}"

        """Можно записать короче, input_data = text_box_page.fill_all_fields() и 
        output_data = text_box_page.check_field_form() и потом сравнить 2 списка, но вариант выше более подробный
        в плане обозначения точного места ошибки"""

class TestCheckBox:
    def test_checkbox(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_checkbox = check_box_page.get_output_results()
        assert input_checkbox == output_checkbox, f"Input: {input_checkbox} differs from output: {output_checkbox}"

class TestRadioButton:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        """Кликаем по радио указывая ключ соответствующий локатору радио кнопки"""
        radio_button_page.click_on_radio_button("yes")
        """И получаем отображаемый текст, с остальными аналогично"""
        output_yes = radio_button_page.get_checked_radio_titles()
        radio_button_page.click_on_radio_button("impressive")
        output_impressive = radio_button_page.get_checked_radio_titles()
        radio_button_page.click_on_radio_button("no")
        output_no = radio_button_page.get_checked_radio_titles()
        assert output_yes == "Yes", '"Yes" radio button haven\'t been selected'
        assert output_impressive == 'Impressive', '"Impressive" radio button haven\'t been selected'
        assert output_no == "No", '"No" radio button haven\'t been selected'

class TestWebTable:

    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_data = web_table_page.check_new_person()
        """Проверяем что данные юзера в массиве юзеров"""
        for person in new_person:
            assert person in table_data, f"User {person} doesn't exist in table data: {table_data}"

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        """Ключ - любой элемент из 0 списка в массиве"""
        key_word = web_table_page.add_new_person()[0][randint(0, 5)]
        """Ищем юзера по ключу и проверяем есть ли этот ключ в таблице"""
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, f"Word {key_word} not contains in {table_result}"
