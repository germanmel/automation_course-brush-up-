from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    #fields
    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, '.rct-title')
    CHECKED_ITEMS = (By.CSS_SELECTOR, '.rct-icon-check')
    ITEM_TITLE = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULTS = (By.CSS_SELECTOR, '.text-success')

