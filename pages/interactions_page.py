import random, time
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage

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
        for i in range(len(item_list)-1):
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








