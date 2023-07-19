import time
import pytest

from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage
from locators.widgets_page_locators import ToolTipsPageLocators


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

    class TestDataPickerPage:

        def test_change_date(self, driver):
            picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            picker_page.open()
            month = picker_page.fill_random_month()
            year = picker_page.fill_random_year()
            day = picker_page.fill_random_day()
            actual_date = picker_page.get_entered_date()
            expected_date = f"{month}/{day}/{year}"
            assert actual_date == expected_date, f"Date {actual_date} differs from expected date {expected_date}"


        def test_change_date_and_time(self, driver):
            picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            picker_page.open()
            timedate_before = picker_page.get_entered_timedate()
            picker_page.fill_datetime_month()
            picker_page.fill_datetime_year()
            picker_page.fill_datetime_day()
            picker_page.fill_datetime_time()
            timedate_after = picker_page.get_entered_timedate()
            assert timedate_before != timedate_after

    class TestSliderPage:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            value_before, value_after = slider_page.drag_slider()
            assert value_before != value_after, f"Slider location doesn't change, before{value_before} after{value_after}"


    class TestProgressBarPage:

        def test_progress_bar_finish(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value, reset_btn = progress_bar_page.check_finish_progress_bar()
            assert value == "100", "Progress bar isn't reached 100%"
            assert reset_btn == "Reset", f"Unexpected reset button title {reset_btn}"


        def test_start_stop_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            stop_value, btn_text = progress_bar_page.check_start_stop_progress_bar()
            assert int(stop_value) < 100, f"Progress bar reached 100%, stop value = {stop_value}"
            assert btn_text == "Start", f"Expected button text 'Start' but actual {btn_text}"

        def test_reset_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before_value, after_value = progress_bar_page.check_reset_btn()
            assert before_value == "0" and after_value == "0"

    class TestTabsPage:

        def test_tabs(self, driver):
            tab_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tab_page.open()
            actual_tabs_title = tab_page.check_tabs()
            expected_tabs_title = ['What,Origin,Use,More']
            assert actual_tabs_title == expected_tabs_title, f"Unexpected tab titles {actual_tabs_title}"

        def test_tabs_content(self, driver):
            tab_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tab_page.open()
            actual_length = tab_page.check_tabs_content()
            expected_length = [574, 1059, 613]
            assert actual_length == expected_length, \
                f"Expected length of content {expected_length} differs from actual {actual_length}"

        @pytest.mark.xfail(reason="Tab is unclickable, task 21324")
        def test_more_tab(self, driver):
            tab_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tab_page.open()
            actual_length = tab_page.check_more_tab()
            expected_length = 145
            assert actual_length == expected_length, \
                f"Expected length of content {expected_length} differs from actual {actual_length}"


    class TestToolTipsPage:
        locators = ToolTipsPageLocators()

        elements = {
            "button": {
                "locator": locators.BUTTON,
                "expected_text": 'You hovered over the Button',
            },
            "field": {
                "locator": locators.FIELD,
                "expected_text": 'You hovered over the text field',
            },
            "contrary": {
                "locator": locators.CONTRARY_LINK,
                "expected_text": 'You hovered over the Contrary',
            },
            "section": {
                "locator": locators.SECTION_LINK,
                "expected_text": 'You hovered over the 1.10.32',
            }
        }

        @pytest.mark.parametrize("element", elements.values(), ids=elements.keys())
        def test_tooltips(self, driver, element):
            tooltips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tooltips_page.open()
            tooltip_text = tooltips_page.check_tooltip(element['locator'])
            expected_text = element['expected_text']
            assert tooltip_text == expected_text, \
                f"Unexpected tooltip text: {tooltip_text}, but it was expected: {expected_text}"

    class TestMenuPage:

        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            btns_text = menu_page.check_menu()
            expected_text = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item',
                             'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
            assert btns_text == expected_text, f"Menu title list: {btns_text} differs from expected: {expected_text}"

    #TODO - сделать тесты по этой вкладке
    class TestSelectMenuPage:

        def test_select(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()

