import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    """Сохраняем профиль пользователя и работаем на нём, при первом запуске с профилем можно добавить таймслип и 
    установить необходимые расширения, например adblock, при следующих запусках будет использоваться этот профиль с 
    расширением"""
    options.add_argument("user-data-dir=C:\\profile")
    """Иницилизируем драйвер с помощью менеджера"""
    driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.16").install(), chrome_options=options)
    driver.maximize_window() #Открываем на весь экран
    yield driver
    driver.quit()