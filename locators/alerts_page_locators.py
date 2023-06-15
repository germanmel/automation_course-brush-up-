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

    # Frames
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAME_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    # Nested frames
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')

    # Modals
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')