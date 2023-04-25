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