from selenium.webdriver.common.by import By

class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, '#demo-tab-list')
    LIST_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-list .list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, '#demo-tab-grid')
    GRID_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-grid .list-group-item')
