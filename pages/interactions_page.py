import random, time
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, locator):
        item_list = self.elements_are_visible(locator)
        return [item.text for item in item_list]

    def change_random_item_order(self, tab, items):
        self.element_is_visible(tab).click()
        order_before = self.get_sortable_items(items)
        item_list = random.sample(self.elements_are_visible(items), k=2)
        what_element = item_list[0]
        where_element = item_list[1]
        self.drag_and_drop_to_element(what_element, where_element)
        order_after = self.get_sortable_items(items)
        return order_before, order_after

    def move_one_to_end(self, tab, items):
        self.element_is_visible(tab).click()
        item_list = self.elements_are_visible(items)
        for i in range(len(item_list)-1):
            self.drag_and_drop_to_element(item_list[i], item_list[i + 1])
        order_after = self.get_sortable_items(items)
        return order_after

class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def select_random_items(self, tab, items, selected):
        self.element_is_visible(tab).click()
        item_list = random.sample(self.elements_are_visible(items), k=3)
        items_for_select = []
        for item in item_list:
            items_for_select.append(item.text)
            item.click()
        time.sleep(4)
        selected_items = self.elements_are_visible(selected)
        selected_names = [item.text for item in selected_items]
        return items_for_select, selected_names

class ResizablePage(BasePage):
    locators = ResizablePageLocators()
