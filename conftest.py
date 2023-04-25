import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install()) #Иницилизируем драйвер с помощью менеджера
    driver.maximize_window() #Открываем на весь экран
    yield driver
    driver.quit()