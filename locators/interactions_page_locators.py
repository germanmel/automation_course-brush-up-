from selenium.webdriver.common.by import By

class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, '#demo-tab-list')
    LIST_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-list .list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, '#demo-tab-grid')
    GRID_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-grid .list-group-item')

class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, '#demo-tab-list')
    LIST_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-list .list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, '#demo-tab-grid')
    GRID_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-grid .list-group-item')
    ACTIVE_LIST_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-list li[class*="active"]')
    ACTIVE_LIST_GRID = (By.CSS_SELECTOR, '#demo-tabpane-grid li[class*="active"]')

class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, '#resizableBoxWithRestriction span[class*="react-resizable-handle"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, '#resizableBoxWithRestriction')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, '#resizable span[class*="react-resizable-handle"]')
    RESIZABLE = (By.CSS_SELECTOR, '#resizable')
