import time

from pages.element_page import TextBoxPage


class TestTextBox:

    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        #  Получаем переменные из return функций по проверке заполнения и заполненных полей
        full_name, email, current_adress, permanent_adress = text_box_page.fill_all_fields()
        output_name, output_email, output_cur_adress, output_per_adress = text_box_page.check_field_form()
        assert full_name == output_name, f"Full name {full_name} differs from output name {output_name}"
        assert email == output_email, f"Email {email} differs from output email {output_email}"
        assert current_adress == output_cur_adress, \
            f'Current adress {current_adress} differs from output cur adress {output_cur_adress}'
        assert permanent_adress == output_per_adress, \
            f"Permanent adress {permanent_adress} differs from output per adress {output_per_adress}"

        """Можно записать короче, input_data = text_box_page.fill_all_fields() и 
        output_data = text_box_page.check_field_form() и потом сравнить 2 списка, но вариант выше более подробный
        в плане обозначения точного места ошибки"""