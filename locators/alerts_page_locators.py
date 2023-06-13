import random

from selenium.webdriver.common.by import By

class AlertPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_PAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    OPENED_PAGE_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
