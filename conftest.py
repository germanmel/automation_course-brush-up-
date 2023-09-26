import pytest
import os
from datetime import datetime
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",  # настраиваем определение параметров командной строки которые можем вводить
                    help="Choose browser: chrome or firefox")

@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption(
        "browser_name")  # с помощью встроенной фикстуры request передаём браузеру параметры
    if browser_name == "chrome":
        options = Options()
        """Сохраняем профиль пользователя и работаем на нём, при первом запуске с профилем можно добавить таймслип и 
        установить необходимые расширения, например adblock, при следующих запусках будет использоваться этот профиль с 
        расширением"""
        options.add_argument("user-data-dir=C:\\profile")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # данная строка отключает логирование в консоли, убирает текст DevTools listening on ws://127.0.0.1 и прочий мусор
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()  # Открываем на весь экран
        print("\nstart chrome browser for test..")
    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox()
        print("\nstart firefox browser for test..")
    else:
        print("--browser_name should be chrome or firefox")
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



