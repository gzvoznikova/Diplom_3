import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from page_objects.main_page import MainPage
from page_objects.recovery_page import RecoveryPassPage
from urls import Urls



@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    if driver_class == webdriver.Chrome:
        options = Options()
        options.add_argument('--window-size=1680,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
    elif driver_class == webdriver.Firefox:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1680')
        firefox_options.add_argument('--height=1080')
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
    driver.get(Urls.base_url)
    yield driver
    driver.quit()

@pytest.fixture
def auth_to_account(driver):
    def login_acc():
        main_page = MainPage(driver)
        recovery_pass = RecoveryPassPage(driver)
        time.sleep(3)
        main_page.click_on_button_login_in_main()
        recovery_pass.send_email()
        recovery_pass.send_password()
        recovery_pass.click_button_login_in_auth()
    return login_acc

