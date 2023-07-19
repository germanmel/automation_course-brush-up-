from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_1 = (By.CSS_SELECTOR, "#section1Heading")
    SECTION_1_CONTENT = (By.CSS_SELECTOR, "#section1Content p")
    SECTION_2 = (By.CSS_SELECTOR, "#section2Heading")
    SECTION_2_CONTENT = (By.CSS_SELECTOR, "#section2Content p")
    SECTION_3 = (By.CSS_SELECTOR, "#section3Heading")
    SECTION_3_CONTENT = (By.CSS_SELECTOR, "#section3Content p")

class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, ".auto-complete__multi-value__label")
    REMOVE_VALUE = (By.CSS_SELECTOR, ".auto-complete__multi-value__remove")
    REMOVE_ALL_VALUE = (By.CSS_SELECTOR, 'div[class*="auto-complete__indicator auto-complete__clear-indicator"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_INPUT_VALUE = (By.CSS_SELECTOR, 'div[class*="auto-complete__single-value"]')

class DataPickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select.react-datepicker__month-select')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select.react-datepicker__year-select')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, '.react-datepicker__day')
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH_SELECT = (By.CSS_SELECTOR, 'span[class="react-datepicker__month-read-view--down-arrow"]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, '.react-datepicker__month-option')
    DATE_AND_TIME_YEAR_SELECT = (By.CSS_SELECTOR, 'span[class="react-datepicker__year-read-view--down-arrow"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, '.react-datepicker__year-option')
    DATE_AND_TIME_SELECT_DAY_LIST = (By.CSS_SELECTOR, '.react-datepicker__day')
    DATE_AND_TIME_SELECT_TIME = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_PREV_MONTH = (By.CSS_SELECTOR,
                                'button[class*="react-datepicker__navigation--previous"]')
    DATE_AND_TIME_NEXT_MONTH = (By.CSS_SELECTOR,
                                'button[class*="react-datepicker__navigation--next"]')

class SliderPageLocators:
    SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, '#sliderValue')

class ProgressBarPageLocators:
    PROGRESS_BAR = (By.CSS_SELECTOR, 'div[role="progressbar"]')
    RESET_BTN = (By.CSS_SELECTOR, '#resetButton')
    START_STOP_BTN = (By.CSS_SELECTOR, '#startStopButton')
    RESET_BTN = (By.CSS_SELECTOR, '#resetButton')

class TabsPageLocators:
    NAV_TABS = (By.CSS_SELECTOR, '.nav-tabs')
    """More некликабельна, поэтому её проверим отдельно"""
    TABS_WITHOUT_MORE = (By.CSS_SELECTOR, 'a[role="tab"]:not(#demo-tab-more)')
    TAB_CONTENT = (By.CSS_SELECTOR, '.tab-content')
    MORE_TAB = (By.CSS_SELECTOR, '#demo-tab-more')

class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, '#toolTipButton')
    FIELD = (By.CSS_SELECTOR, '#texFieldToolTopContainer input')
    CONTRARY_LINK = (By.XPATH, '//*[text()="Contrary"]')
    SECTION_LINK = (By.XPATH, '//*[text()="1.10.32"]')
    TOOLTIPS = (By.CSS_SELECTOR, '.tooltip-inner')

class MenuPageLocators:
    MENU_ITEMS_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')



