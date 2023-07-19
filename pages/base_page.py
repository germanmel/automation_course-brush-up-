import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



"""Базовый класс страницы, который будем использовать везде"""

class BasePage:
    """Метод инициализирует аргументы при каждом вызове экземпляра класса"""

    #pytest.fixture()
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    """Метод открытия страницы"""
    def open(self):
        self.driver.get(self.url)

    """Элемент виден на странице"""
    # def element_is_visible(self, locator, timeout=5):
    #     return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    """Элементы видны на странице"""
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    """Элемент присутствует в dom дереве(может быть не виден, но он есть)"""
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    """Элементы присутствуют в dom дереве"""
    def elements_are_present(self, locator, timeout=5):
        try:
            return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return False

    """Элемент не виден на странице"""
    def element_is_not_visible(self, locator, timeout=5):
        try:
            return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))
        except TimeoutException:
            return False
    """Элемент кликабелен"""
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """Скролл страницы к элементу"""
    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """Перемещение мыши к элементу"""
    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    """Двойной клик по элементу"""
    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    """Правый клик по элементу"""
    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    """Убрать футер со страницы"""
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementsById('close-fixedban').remove();")

    """Переключиться на окно по индексу"""
    def switch_to_window(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    """Открывает новую пустую вкладку или новое окно и фокусируется на нём (не нужно явно указывать)"""
    def open_new_clear_page(self, view=None):  # view can be "tab" or "window"
        self.driver.switch_to.new_window(view)

    """Переключиться на iframe"""
    def switch_to_frame(self, element):
        self.driver.switch_to.frame(element)

    """Схватить и тянуть по оси координат"""
    def drag_and_drop_by_offset(self, element, x_coord, y_coord):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    """Схватить и тянуть к элементу"""
    def drag_and_drop_to_element(self, what_element, where_element):
        action = ActionChains(self.driver)
        action.drag_and_drop(what_element, where_element)
        action.perform()










