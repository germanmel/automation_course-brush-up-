import time

from pages.form_page import FormPage


class TestFormPage:

    def test_filled_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        p = form_page.fill_form()
        result = form_page.form_resul()
        expected = [p.firstname + " " + p.lastname, p.email]
        actual = [result[0], result[1]]
        assert expected == actual, f"Expected result: {expected} differs from actual ressult: {actual}"


