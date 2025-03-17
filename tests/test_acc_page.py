from conftest import *
import allure
from urls import Urls
from page_objects.account_page import AccountPage
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage

class TestAccountPage:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_click_to_account_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_personal_account_in_header()
        assert main_page.is_current_url(Urls.login_urls)

    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_navigate_to_order_history_page_success(self, driver, auth_to_account):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OrderFeedPage(driver)
        auth_to_account()
        main_page.click_on_personal_account_in_header()
        account_page.click_on_order_history_button()
        order_history_page.wait_visibility_of_order_card()
        assert 'бургер' in order_history_page.get_text_of_order_card_title()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_from_account_page_success(self, driver, auth_to_account):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        auth_to_account()
        main_page.click_on_personal_account_in_header()
        account_page.wait_visibility_of_description()
        account_page.click_on_logout_button()
        account_page.wait_visibility_of_button_register()
        assert account_page.check_displaying_of_button_register()