import time

import pytest

from pages.alerts_page import AlertsPage


class TestAlerts:
    class TestBrowserWindow:

        types = ["Tab", "Page"]
        @pytest.mark.parametrize("type", types)
        def test_open_pages(self, driver, type):
            new_tab_page = AlertsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            result_text = new_tab_page.check_opened_new_page(type)
            expected_text = "This is a sample page"
            assert result_text == expected_text, f"Opened page text {result_text} differs from {expected_text}"

        """Пример работы открытия новых вкладок/окон"""
        def test_open(self, driver):
            new_tab_page = AlertsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_tab_page.open_new_clear_page("tab")
            time.sleep(2)
            new_tab_page.open_new_clear_page("tab")
            time.sleep(2)
            new_tab_page.open_new_clear_page("window")
            time.sleep(2)

    class TestAlerts:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            actual_alert_text = alert_page.check_see_alert()
            expected_text = "You clicked a button"
            assert actual_alert_text == expected_text, f"Text {actual_alert_text} " \
                                                       f"differs from expected text: {expected_text}"
        def test_alert_appear_5sec(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            actual_alert_text = alert_page.check_alert_appear_5sec()
            expected_text = "This alert appeared after 5 seconds"
            assert actual_alert_text == expected_text, f"Text {actual_alert_text} " \
                                                       f"differs from expected text: {expected_text}"

        def test_alert_confirm(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            actual_result_text = alert_page.check_confirm_alert()
            expected_text = "You selected Ok"
            assert actual_result_text == expected_text, f"Text {actual_result_text} " \
                                                       f"differs from expected text: {expected_text}"
        def test_promt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            actual_result_text, expected_text = alert_page.check_promt_alert()
            assert actual_result_text.split(" ")[2] == expected_text, f"Text {actual_result_text} " \
                                                       f"differs from expected text: {expected_text}"

    class TestFrames:

        def test_frames(self, driver):
            frame_page = AlertsPage(driver, "https://demoqa.com/frames")
            frame_page.open()
            actual_result1 = frame_page.check_frame('frame1')
            expected_result1 = ['This is a sample page', '500px', '350px']
            actual_result2 = frame_page.check_frame("frame2")
            expected_result2 = ['This is a sample page', '100px', '100px']
            assert actual_result1 == expected_result1, "The frame1 doesn't exist or incorrect"
            assert actual_result2 == expected_result2, "The frame2 doesn't exist or incorrect"

    class TestNestedFrames:

        def test_nested_frames(self, driver):
            nested_frame_page = AlertsPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            actual_parent_text, actual_child_text = nested_frame_page.check_nested_frames()
            expected_parent_text = "Parent frame"
            expected_child_text = "Child Iframe"
            assert actual_parent_text == expected_parent_text, "Parent text is incorrect"
            assert actual_child_text == expected_child_text, "Child text is incorrect"

    class TestModal:

        def test_small_modal(self, driver):
            modal_page = AlertsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_page.open()
            actual_title, actual_text = modal_page.check_small_modal()
            expected_title = "Small Modal"
            expected_text = "This is a small modal. It has very less content"
            assert actual_title == expected_title
            assert actual_text == expected_text

        def test_large_modal(self, driver):
            modal_page = AlertsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_page.open()
            actual_title, actual_text = modal_page.check_large_modal()
            expected_title = "Large Modal"
            expected_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
                            "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, " \
                            "when an unknown printer took a galley of type and scrambled it to make a type specimen " \
                            "book. It has survived not only five centuries, but also the leap into electronic " \
                            "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the " \
                            "release of Letraset sheets containing Lorem Ipsum passages, and more recently with " \
                            "desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            assert actual_title == expected_title
            assert actual_text == expected_text




