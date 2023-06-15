import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("user-data-dir=C:\\profile")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) #Иницилизируем драйвер с
    # помощью менеджера
    driver.maximize_window() #Открываем на весь экран
    yield driver
    driver.quit()