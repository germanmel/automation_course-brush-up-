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
