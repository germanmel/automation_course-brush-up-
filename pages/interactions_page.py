import random, time
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Страница сортировки перетягиванием(пятнашки)
class SortablePage(BasePage):
    locators = SortablePageLocators()
    """Получаем все элементы которые можно сортировать"""

    def get_sortable_items(self, locator):
        item_list = self.elements_are_visible(locator)
        return [item.text for item in item_list]

    def change_random_item_order(self, tab, items):
        self.element_is_visible(tab).click()
        order_before = self.get_sortable_items(items)
        """Берём 2 рандомных элемента списка"""
        item_list = random.sample(self.elements_are_visible(items), k=2)
        what_element = item_list[0]
        where_element = item_list[1]
        """Перетягиваем один на другой"""
        self.drag_and_drop_to_element(what_element, where_element)
        order_after = self.get_sortable_items(items)
        return order_before, order_after

    """"""

    def move_one_to_end(self, tab, items):
        self.element_is_visible(tab).click()
        item_list = self.elements_are_visible(items)
        for i in range(len(item_list) - 1):
            self.drag_and_drop_to_element(item_list[i], item_list[i + 1])
        order_after = self.get_sortable_items(items)
        return order_after


# Страница множественного выбора
class SelectablePage(BasePage):
    locators = SelectablePageLocators()
    """Получаем несколько рандомных элементов из списка, кликаем по ним, возвращаем кликнутые и активные для проверки"""

    def select_random_items(self, tab, items, selected):
        self.element_is_visible(tab).click()
        item_list = random.sample(self.elements_are_visible(items), k=3)
        items_for_select = []
        for item in item_list:
            items_for_select.append(item.text)
            item.click()
        selected_items = self.elements_are_visible(selected)
        selected_names = [item.text for item in selected_items]
        return items_for_select, selected_names


# Страница изменения размера окон
class ResizablePage(BasePage):
    locators = ResizablePageLocators()
    """Вспомогательный метод получения размера окна"""

    def get_size(self, window_locator):
        window = self.element_is_visible(window_locator)
        window_size = window.size
        return window_size

    """Получаем дефолтный размер окна, увеличиваем его больше максимума, уменьшаем меньше минимума,
    возвращаем размеры для проверки"""

    def change_resizable_box_size(self):
        default_size = self.get_size(self.locators.RESIZABLE_BOX)
        handle = self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE)
        self.drag_and_drop_by_offset(handle, -300, -200)
        min_size = self.get_size(self.locators.RESIZABLE_BOX)
        self.drag_and_drop_by_offset(handle, 500, 500)
        max_size = self.get_size(self.locators.RESIZABLE_BOX)
        return default_size, min_size, max_size

    """Аналогично методу выше, но тут нет границ, поэтому просто меняем размеры и возвращаем для проверки"""

    def change_resizable_size(self):
        default_size = self.get_size(self.locators.RESIZABLE)
        handle = self.element_is_visible(self.locators.RESIZABLE_HANDLE)
        self.drag_and_drop_by_offset(handle, -350, -350)
        min_size = self.get_size(self.locators.RESIZABLE)
        self.drag_and_drop_by_offset(handle, 500, 500)
        max_size = self.get_size(self.locators.RESIZABLE)
        return default_size, min_size, max_size


# Страница drag&drop элементов
class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drag_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP)
        text_before = drop_div.text
        self.drag_and_drop_to_element(drag_div, drop_div)
        text_after = drop_div.text
        return text_before, text_after

    def drag_accept(self, drag_locator):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visible(drag_locator)
        drop_div = self.element_is_visible(self.locators.ACCEPT_DROP)
        text_before = drop_div.text
        self.drag_and_drop_to_element(drag_div, drop_div)
        text_after = drop_div.text
        return text_before, text_after

    """Метод принимает локатор дива в который перетаскиваем элемент и локатор соседского дива для проверки правильного
     изменения текста в обоих дивах контейнера, получаем текст до, перетягиваем, получаем текст после, сравниваем в 
     тесте"""

    def drag_prevent(self, drop_locator, neighbor_locator):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        drag_div = self.element_is_visible(self.locators.PREVENT_DRAG)
        drop_div = self.element_is_visible(drop_locator)
        neighbor_div = self.element_is_visible(neighbor_locator)
        text_before = [drop_div.text, neighbor_div.text]
        self.drag_and_drop_to_element(drag_div, drop_div)
        text_after = [drop_div.text, neighbor_div.text]
        return text_before, text_after

    def drag_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_div = self.element_is_visible(self.locators.REVERTABLE_DRAG)
        drop_div = self.element_is_visible(self.locators.REVERT_DROP)
        text_before = drop_div.text
        self.drag_and_drop_to_element(drag_div, drop_div)
        location_before = drag_div.get_attribute("style")
        text_after = drop_div.text
        # Ждём и проверяем что элемент вернулся на место
        WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element_attribute(self.locators.REVERTABLE_DRAG,
                                                                                       "style",
                                                                                       "position: relative; left: 0px; top: 0px;"))
        location_after = drag_div.get_attribute("style")
        return text_before, location_before, text_after, location_after

    def drag_not_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_div = self.element_is_visible(self.locators.NOT_REVERTABLE_DRAG)
        drop_div = self.element_is_visible(self.locators.REVERT_DROP)
        other_drag = self.element_is_visible(self.locators.REVERTABLE_DRAG)
        text_before = drop_div.text
        location_before = drag_div.get_attribute("style")
        self.drag_and_drop_to_element(drag_div, drop_div)
        text_after = drop_div.text
        location_after = drag_div.get_attribute("style")
        self.drag_and_drop_to_element(drag_div, other_drag)
        location_leave_div = drag_div.get_attribute("style")
        return text_before, location_before, text_after, location_after, location_leave_div


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    def move_drag_element(self, tab_locator, drag_locator):
        self.element_is_visible(tab_locator).click()
        drag_div = self.element_is_visible(drag_locator)
        self.drag_and_drop_by_offset(drag_div, 50, 50)
        location_before = drag_div.get_attribute("style")
        self.drag_and_drop_by_offset(drag_div, 50, 50)
        location_after = drag_div.get_attribute("style")
        return location_before, location_after

    def drag_simple(self):
        tab = self.locators.SIMPLE_TAB
        drag = self.locators.DRAG_ME
        location_before, location_after = self.move_drag_element(tab, drag)
        return location_before, location_after

    def drag_axis_x(self):
        tab = self.locators.AXIS_RESTRICTED_TAB
        drag = self.locators.X_ELEMENT
        location_before, location_after = self.move_drag_element(tab, drag)
        return location_before, location_after

    def drag_axis_y(self):
        tab = self.locators.AXIS_RESTRICTED_TAB
        drag = self.locators.Y_ELEMENT
        location_before, location_after = self.move_drag_element(tab, drag)
        return location_before, location_after

#TODO: Избавиться от дублирующего кода, напр. параметризацией
    def drag_box_inside_container(self, size=None):
        self.element_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()
        container = self.element_is_present(self.locators.CONTAINER_BOX_DIV)
        drag_element = self.element_is_visible(self.locators.DRAG_BOX)
        # начальные координаты элемента
        start_x = drag_element.location['x']
        start_y = drag_element.location['y']
        # перемещаем элемент
        self.drag_and_drop_by_offset(drag_element, 700, 700)
        if size == "small":
            self.change_window_size(1024, 768)
        # конечные координаты элемента
        end_x = drag_element.location['x']
        end_y = drag_element.location['y']
        # координаты и размер контейнера
        container_x = container.location['x']
        container_y = container.location['y']
        container_width = container.size['width']
        container_height = container.size['height']

        return end_x, end_y, container_x, container_y, container_width, container_height

    def drag_span_inside_container(self, size=None):
        self.element_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()
        container = self.element_is_present(self.locators.CONTAINER_SPAN_DIV)
        drag_element = self.element_is_visible(self.locators.DRAG_SPAN)
        # начальные координаты элемента
        start_x = drag_element.location['x']
        start_y = drag_element.location['y']
        # перемещаем элемент
        self.drag_and_drop_by_offset(drag_element, 100, 100)
        if size == "small":
            self.change_window_size(1024, 768)
        # конечные координаты элемента
        end_x = drag_element.location['x']
        end_y = drag_element.location['y']
        # координаты и размер контейнера
        container_x = container.location['x']
        container_y = container.location['y']
        container_width = container.size['width']
        container_height = container.size['height']

        return end_x, end_y, container_x, container_y, container_width, container_height
