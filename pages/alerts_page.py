import random
import time

from pages.base_page import BasePage
from locators.alerts_page_locators import AlertPageLocators


class AlertsPage(BasePage):
    locators = AlertPageLocators()

    def check_opened_new_page(self, button_type="Tab"):
        if button_type == "Tab":
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
            self.switch_to_window(1)
            text_title = self.element_is_present(self.locators.OPENED_PAGE_TEXT).text
            return text_title
        elif button_type == "Page":
            self.element_is_visible(self.locators.NEW_PAGE_BUTTON).click()
            self.switch_to_window(1)
            text_title = self.element_is_present(self.locators.OPENED_PAGE_TEXT).text
            return text_title

        else:
            print("Error! button_type can be only Tab or Page")

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert_text

    def check_alert_appear_5sec(self):
            self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5SEC_BUTTON).click()
            time.sleep(5)
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            return alert_text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        """Переключаемся на алерт и подтверждаем его"""
        alert = self.driver.switch_to.alert
        alert.accept()
        result_text = self.element_is_visible(self.locators.CONFIRM_ALERT_TEXT).text
        return result_text

    def check_promt_alert(self):
        text = f"Test{random.randint(0,999)}"
        self.element_is_visible(self.locators.PROMT_BOX_ALERT_BUTTON).click()
        """Переключаемся на алерт, вводим текст и подтверждаем"""
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        result_text = self.element_is_visible(self.locators.PROMT_RESULT).text
        return result_text, text

    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return [text, width, height]

        if frame_num == "frame2":
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            return [text, width, height]


