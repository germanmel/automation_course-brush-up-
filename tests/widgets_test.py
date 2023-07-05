from pages.widgets_page import AccordianPage


class TestWidgets:

    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian(1)
            second_title, second_content = accordian_page.check_accordian(2)
            third_title, third_content = accordian_page.check_accordian(3)
            first_expected_title = "What is Lorem Ipsum?"
            second_expected_title = "Where does it come from?"
            third_expected_title = "Why do we use it?"
            assert first_title == first_expected_title and len(first_content) > 0
            assert second_title == second_expected_title and len(second_content) > 0
            assert third_title == third_expected_title and len(third_content) > 0

