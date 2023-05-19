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
    ITEM_TITLE = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULTS = (By.CSS_SELECTOR, '.text-success')

class RadioButtonLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, '.custom-control-label[for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, '.custom-control-label[for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, '.custom-control-label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')

class WebTableLocators:
    #add person form
    ADD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, '#age')
    SALARY_INPUT = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, '#department')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    #table
    FULL_PERSONS_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')

    #update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')