import random

from selenium.webdriver.common.by import By

class AlertPageLocators:
    # Windows page
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_PAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    OPENED_PAGE_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    # Alerts page
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_AFTER_5SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"')
    CONFIRM_ALERT_TEXT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


