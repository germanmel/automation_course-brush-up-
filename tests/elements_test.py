import time

import allure
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    FilePage, DynamicPropertiesPage
from random import randint
from locators.elements_page_locators import LinkPageLocators

@allure.suite("Elements")
class TestTextBox:
    @allure.title("Check TextBox")
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
    @allure.title("Check CheckBox")
    def test_checkbox(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_checkbox = check_box_page.get_output_results()
        assert input_checkbox == output_checkbox, f"Input: {input_checkbox} differs from output: {output_checkbox}"

class TestRadioButton:
    @allure.title("Check RadioButton")
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
    @allure.title("Check WebTable add person")
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_data = web_table_page.check_new_person()
        """Проверяем что данные юзера в массиве юзеров"""
        for person in new_person:
            assert person in table_data, f"User {person} doesn't exist in table data: {table_data}"

    @allure.title("Check WebTable search person")
    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        """Ключ - любой элемент из 0 списка в массиве"""
        key_word = web_table_page.add_new_person()[0][randint(0, 5)]
        """Ищем юзера по ключу и проверяем есть ли этот ключ в таблице"""
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, f"Word {key_word} not contains in {table_result}"

    @allure.title("Check WebTable update person information")
    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        """Создаём юзера и сохраняем фамилию"""
        lastname = web_table_page.add_new_person()[0][1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert str(age) in row, f"Age {age} doesn't exist in user data {row}"

    @allure.title("Check WebTable delete person")
    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[0][3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted_person()
        time.sleep(2)
        assert text == "No rows found", f"Text {text} differs from expexted 'No rows found"

    @allure.title("Check WebTable change count")
    def test_web_table_change_count(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count, options = web_table_page.select_up_to_some_rows()
        assert count == options

    def test_web_table_change_count_reverse(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count, options = web_table_page.select_up_to_some_rows_reverse()
        assert count == options

class TestButtonPage:

    def test_different_click_on_the_buttons(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        double = button_page.click_on_different_button("double")
        right = button_page.click_on_different_button("right")
        click = button_page.click_on_different_button("click")
        assert double == 'You have done a double click', f"Success text for double click: {double} isn't correct"
        assert right == 'You have done a right click', f"Success text for right click: {right} isn't correct"
        assert click == 'You have done a dynamic click', f"Success text for click me: {click} isn't correct"

class TestLinksPage:

    locators = LinkPageLocators()
    """Проверяем что новая вкладка открывается на домашней"""
    def test_home_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        tab_url = links_page.check_new_tab_link(self.locators.SIMPLE_HOME_LINK)
        base_url = 'https://demoqa.com/'
        print(tab_url)
        print(base_url)
        assert tab_url == base_url, f"Tab url {tab_url} is incorrect, expected {base_url}"

    def test_home_link_dynamic(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        tab_url = links_page.check_new_tab_link(self.locators.DYNAMIC_HOME_LINK)
        base_url = 'https://demoqa.com/'
        print(tab_url)
        print(base_url)
        assert tab_url == base_url, f"Tab url {tab_url} is incorrect, expected {base_url}"


    def test_created_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_link_status('https://demoqa.com/created', self.locators.CREATED)
        expected_code = 201
        print(response_code)
        print(expected_code)
        assert response_code == expected_code, f"Response code: {response_code}, expected {expected_code}"

    def test_no_content_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_link_status('https://demoqa.com/no-content', self.locators.NO_CONTENT)
        expected_code = 204
        print(response_code)
        print(expected_code)
        assert response_code == expected_code, f"Response code: {response_code}, expected {expected_code}"

    def test_moved_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_link_status('https://demoqa.com/moved', self.locators.MOVED)
        expected_code = 301
        print(response_code)
        print(expected_code)
        assert response_code == expected_code, f"Response code: {response_code}, expected {expected_code}"

    def test_bad_request_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_link_status('https://demoqa.com/bad-request', self.locators.BAD_REQUEST)
        expected_code = 400
        print(response_code)
        print(expected_code)
        assert response_code == expected_code, f"Response code: {response_code}, expected {expected_code}"

    def test_unauthorized_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_link_status('https://demoqa.com/unauthorized', self.locators.UNAUTHORIZED)
        expected_code = 401
        print(response_code)
        print(expected_code)
        assert response_code == expected_code, f"Response code: {response_code}, expected {expected_code}"

    def test_forbidden_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_link_status('https://demoqa.com/forbidden', self.locators.FORBIDDEN)
        expected_code = 403
        print(response_code)
        print(expected_code)
        assert response_code == expected_code, f"Response code: {response_code}, expected {expected_code}"

    def test_not_found_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_link_status('https://demoqa.com/invalid-url', self.locators.NOT_FOUND)
        expected_code = 404
        print(response_code)
        print(expected_code)
        assert response_code == expected_code, f"Response code: {response_code}, expected {expected_code}"

class TestFilePage:
    """Загрузка файла как сделано в курсе"""
    def test_upload_file(self, driver):
        file_page = FilePage(driver, 'https://demoqa.com/upload-download')
        file_page.open()
        file_name, text = file_page.upload_file()
        assert file_name == text, f"File name on page: {text} differs from upload file name: {file_name}"

    """Загрузка файла созданного во временной директории, самостоятельная работа"""
    def test_upload_file_from_tmp(self, driver, tmp_path):
        file_page = FilePage(driver, 'https://demoqa.com/upload-download')
        file_page.open()
        file_name, text = file_page.upload_file_from_tmp_directory(tmp_path)
        assert file_name == text, f"File name on page: {text} differs from upload file name: {file_name}"



    def test_download_file(self, driver):
        file_page = FilePage(driver, 'https://demoqa.com/upload-download')
        file_page.open()
        check = file_page.download_file()
        assert check is True, "The file hasn't been downloaded"

@pytest.mark.xfail(reason="Failed due to too long loading page")
class TestDynamicPropertiesPage: # Проверить тесты после решения проблемы с загрузкой страницы из-за рекламы

    def test_change_button_color(self, driver):
        dynamic_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_page.open()
        color_before, color_after = dynamic_page.check_changed_of_color()
        assert color_after != color_before, "Color of button hasn't been changed"

    def test_appear_button(self,driver):
        dynamic_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_page.open()
        appear = dynamic_page.check_appear_of_button()
        assert appear is True







