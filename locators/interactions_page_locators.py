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

class DroppablePageLocators:
    #Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-simple')
    SIMPLE_DRAG = (By.CSS_SELECTOR, '#draggable')
    SIMPLE_DROP = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    #Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, '#acceptable')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, '#notAcceptable')
    ACCEPT_DROP = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    #Prevent Propogation
    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-preventPropogation')
    PREVENT_DRAG = (By.CSS_SELECTOR, '#dragBox')
    PREVENT_NOT_GREEDY_OUTER = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    PREVENT_NOT_GREEDY_INNER = (By.CSS_SELECTOR, '#notGreedyInnerDropBox')
    PREVENT_GREEDY_OUTER = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    PREVENT_GREEDY_INNER = (By.CSS_SELECTOR, '#greedyDropBoxInner')

    #Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-revertable')
    REVERTABLE_DRAG = (By.CSS_SELECTOR, '#revertable')
    NOT_REVERTABLE_DRAG = (By.CSS_SELECTOR, '#notRevertable')
    REVERT_DROP = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')
