import os
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_person, generated_file, generated_file_tmp_directory
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxLocators, RadioButtonLocators, \
    WebTableLocators, ButtonsPageLocators, LinkPageLocators, FilePageLocators
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

class WebTablePage(BasePage):
    locators = WebTableLocators()

    def add_new_person(self, count=1):
        """В метод передаём количество юзеров для создания, генерируем данные в цикле и отправляем в поля,
        после создания юзера добавляем в массив список данных юзера"""
        new_persons = []
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            """Возвращаем в виде списка элементов(по умолчанию tuple), меняем тип данных для соответствия проверке,
            добавляем в список new_person список каждого юзера, если их несколько"""
            new_persons.append([firstname, lastname, str(age), email, str(salary), department])
        return new_persons

    def check_new_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        person_data = []
        for person in person_list:
            """Проходим по каждой строке списка и получаем текст из неё,
            с помощью splitlines() разделяя слова символом новой строки избавляясь от '\n' в списке"""
            person_data.append(person.text.splitlines())
        return person_data

    def search_some_person(self, key_word):
        """Отправляем в строку поиска ключ"""
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)


    def check_search_person(self):
        """Сохраняем кнопку удаления в переменную"""
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        """Находим строку с данными по строке с кнопкой delete"""
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_clickable(self.locators.UPDATE_BUTTON).click()
        input = self.element_is_visible(self.locators.AGE_INPUT)
        input.clear()
        input.send_keys(age)
        submit = self.element_is_visible(self.locators.SUBMIT)
        submit.click()
        return age

    def delete_person(self):
        self.element_is_clickable(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = []
        """Находим дропдаун"""
        element = self.element_is_visible(self.locators.CHANGE_ROWS_DROPDOWN)
        """Генерируем список значений из селектора"""
        options = [i.get_attribute('value') for i in element.find_elements(By.TAG_NAME, 'option')]
        dropdown = Select(element)
        """Кликаем по каждому элементу списка и считаем строки"""
        for option in options:
            dropdown.select_by_value(option)
            count.append(str(self.check_count_rows()))
        return count, options

    def select_up_to_some_rows_reverse(self):
        count = []
        """Находим дропдаун"""
        element = self.element_is_clickable(self.locators.CHANGE_ROWS_DROPDOWN)
        """Генерируем список значений из селектора и разворачиваем его"""
        options = [i.get_attribute('value') for i in element.find_elements(By.TAG_NAME, 'option')]
        options.reverse()
        dropdown = Select(element)
        """Кликаем по каждому элементу списка и считаем строки"""
        for option in options:
            dropdown.select_by_value(option)
            count.append(str(self.check_count_rows()))  # Строки т.к. генерируем опции строковыми атрибутами value
        return count, options

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):

    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.double_click(self.element_is_clickable(self.locators.DOUBLE_CLICK_BUTTON))
            return self.get_clickled_buttons_text(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.right_click(self.element_is_clickable(self.locators.RIGHT_CLICK_BUTTON))
            return self.get_clickled_buttons_text(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_clickable(self.locators.CLICK_ME_BUTTON).click()
            return self.get_clickled_buttons_text(self.locators.SUCCESS_CLICK_ME)


    def get_clickled_buttons_text(self, element):
        return self.element_is_present(element).text

class LinksPage(BasePage):

    locators = LinkPageLocators()
    """Метод получает ссылку из элемента, открывает новую вкладку(указывает селену работать с ней handles[1]
    и получает текущий url вкладки для сравнения в тесте"""
    def check_new_tab_link(self, locator):
        simple_link = self.element_is_visible(locator)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            tab_url = self.driver.current_url
            return tab_url

        else:
            return request.status_code
    """Метод принимает ссылку и локатор кнопки"""
    def check_link_status(self, url, locator):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(locator).click()
        else:
            return request.status_code

class FilePage(BasePage):

    locators = FilePageLocators()

    def upload_file(self):
        """Генерируем файл, получаем путь и его имя"""
        file_name, path = generated_file()
        """Отправляем файл в инпут"""
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        """Удаляем файл, для метода ниже с временной директорией не актуально"""
        os.remove(path)
        """Получаем путь отображаемый после загрузки файла, отсекаем всё кроме имени файла"""
        text = str(self.element_is_visible(self.locators.UPLOADED_RESULT).text)
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def upload_file_from_tmp_directory(self, tmp_path):
        file_name, path = generated_file_tmp_directory(tmp_path)
        print(file_name)
        print(path)
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(f'{path}\{file_name}')
        time.sleep(5)
        text = str(self.element_is_visible(self.locators.UPLOADED_RESULT).text)
        return file_name.split('\\')[-1], text.split('\\')[-1]




