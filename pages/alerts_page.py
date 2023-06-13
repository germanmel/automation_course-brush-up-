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


