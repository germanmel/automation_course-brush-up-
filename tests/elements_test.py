import time

from pages.element_page import TextBoxPage

class TestTextBox:

    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        text_box_page.fill_all_fields()
        output_name, output_email, output_cur_adress, output_per_adress = text_box_page.check_field_form()
        print(output_name, output_email, output_cur_adress, output_per_adress)