import time

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:
    class TestAccordianPage:
        # Тест страницы с аккордеоном
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian(1)
            second_title, second_content = accordian_page.check_accordian(2)
            third_title, third_content = accordian_page.check_accordian(3)
            first_expected_title = "What is Lorem Ipsum?"
            second_expected_title = "Where does it come from?"
            third_expected_title = "Why do we use it?"
            assert first_title == first_expected_title and len(first_content) > 0, "Incorrect title or missing text"
            assert second_title == second_expected_title and len(second_content) > 0, "Incorrect title or missing text"
            assert third_title == third_expected_title and len(third_content) > 0, "Incorrect title or missing text"

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            expected_colors = autocomplete_page.check_multi_input()
            actual_colors = autocomplete_page.get_actual_colors()
            assert actual_colors == expected_colors, f"Actual colors {actual_colors} differ from entered colors " \
                                                     f"{expected_colors}"

        def test_remove_colors(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.check_multi_input()
            autocomplete_page.remove_colors()
            actual_colors = autocomplete_page.get_actual_colors()
            assert actual_colors is False, f"Colors aren't removed: {actual_colors}"

        def test_remove_all_colors(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.check_multi_input()
            autocomplete_page.remove_all_colors()
            actual_colors = autocomplete_page.get_actual_colors()
            assert actual_colors is False, f"Colors aren't removed: {actual_colors}"

        def test_fill_single_autocomplete(selfs, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            actual_color = autocomplete_page.fill_single_input()
            expected_color = autocomplete_page.check_color_in_single()
            assert actual_color == expected_color, f"Actual color {actual_color} differ from entered color {expected_color}"
