import pytest
import os
from datetime import datetime
import allure
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import logging

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",  # настраиваем определение параметров командной строки которые можем вводить
                    help="Choose browser: chrome or firefox")

@pytest.fixture(scope='function')
def driver(request: pytest.FixtureRequest):
    browser_name = request.config.getoption(
        "browser_name")  # с помощью встроенной фикстуры request передаём браузеру параметры
    if browser_name == "local_chrome":
        options = webdriver.ChromeOptions()
        """Сохраняем профиль пользователя и работаем на нём, при первом запуске с профилем можно добавить таймслип и
        установить необходимые расширения, например adblock, при следующих запусках будет использоваться этот профиль 
        из директории с расширением"""
        options.add_argument("user-data-dir=C:\\profile")
        """Отключаем логирование в консоли, убирает текст DevTools listening on ws://127.0.0.1 и прочий мусор"""
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--log-level=3')
        options.add_argument("--headless")
        #options.set_capability("browserVersion", "127")  # Для избавления от мусорных логов
        # https://github.com/SeleniumHQ/selenium/issues/13095

        driver = webdriver.Chrome(options=options)
        # driver.set_window_size(1920, 1080)
        driver.maximize_window()  # Открываем на весь экран
        print("\nstart local chrome browser for test..")

    elif browser_name == "docker_chrome":
        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "127")
        selenoid_options = {
            "enableVNC": True,
            "enableVideo": False,
            "videoName": f"{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]}.mp4",
            "name": os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
        }
        options.set_capability("selenoid:options", selenoid_options)


        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options)
        print("\nstart selenoid chrome browser for test..")

    elif browser_name == "local_firefox":
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
        print("\nstart local firefox browser for test..")

    elif browser_name == "docker_firefox":
        firefox_options = webdriver.FirefoxOptions()
        selenoid_options = {
            "browserName": "firefox",
            "browserVersion": "124.0",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False,
                "videoName": f"{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]}.mp4",
                "name": os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
            }
        }

        for key, value in selenoid_options.items():
            firefox_options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=firefox_options)
        print("\nstart selenoid firefox browser for test..")

    elif browser_name == "docker_opera":
        opera_options = webdriver.ChromeOptions()  # opera это хромиум, поэтому используется хром опции
        selenoid_options = {
            "browserName": "opera",
            "browserVersion": "109.0",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False,
                 "videoName": f"{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]}.mp4",
                 "name": os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
            }
        }

        for key, value in selenoid_options.items():
            opera_options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=opera_options)
        print("\nstart selenoid opera browser for test..")

    else:
        print("--browser_name should be local_chrome,docker_chrome,local_firefox,docker_firefox or docker_opera")
    yield driver
    print("\nquit browser..")
    driver.quit()

#Фикстура сохранения скриншота в случае падения теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        # Тест провалился, создаем скриншот
        driver = item.funcargs['driver']  # Получаем драйвер из фикстуры
        screenshot_dir = "screenshots"  # указываем папку
        os.makedirs(screenshot_dir, exist_ok=True)  # если папка уже создана продолжаем
        """Создаём уникальное имя указывая дату и время, удаляем : т.к. с ними не может быть имени в windows"""
        screenshot_name = os.path.join(screenshot_dir, f"screenshot {datetime.now()}.png".replace(":", ""))
        screenshot = driver.get_screenshot_as_png()
        with open(screenshot_name, "wb") as screenshot_file:
            screenshot_file.write(screenshot)
        allure.attach.file(screenshot_name, name="Скриншот", attachment_type=allure.attachment_type.PNG)



