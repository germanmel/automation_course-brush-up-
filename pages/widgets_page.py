from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {1:
                         {"title": self.locators.SECTION_1,
                          "content": self.locators.SECTION_1_CONTENT},
                     2:
                         {"title": self.locators.SECTION_2,
                          "content": self.locators.SECTION_2_CONTENT},
                     3:
                         {"title": self.locators.SECTION_3,
                          "content": self.locators.SECTION_3_CONTENT},
                     }
        section_title = self.element_is_present(accordian[accordian_num]["title"])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]["content"]).text
        return section_title.text, section_content
