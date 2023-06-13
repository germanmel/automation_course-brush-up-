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
