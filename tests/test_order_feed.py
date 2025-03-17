from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage
from page_objects.account_page import AccountPage
from conftest import *
import allure


class TestFeedPage:

    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    def test_modal_order_details_success(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_header_feed_button()
        order_feed_page.click_on_order_card()
        assert 'бургер' in order_feed_page.get_text_on_title_of_modal_order()


    @allure.title('Проверка отображения существующего заказа из истории пользователя в ленте заказов')
    def test_user_order_history_visible_in_feed(self, driver, auth_to_account):
        main_page = MainPage(driver)
        acc_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        auth_to_account()
        main_page.create_order_in_main()
        main_page.open_main_page()
        main_page.click_on_personal_account_in_header()
        acc_page.click_on_order_history_button()
        order_from_history = order_feed_page.get_last_order_history()
        order_feed_page.open_order_feed_page()
        assert order_feed_page.get_check_number_order(order_from_history)

    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов')
    def test_changes_counter_full_orders_success(self, driver, auth_to_account):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        auth_to_account()
        main_page.click_header_feed_button()
        count_1 = order_feed_page.get_quantity_of_orders()
        main_page.create_order_in_main()
        order_feed_page.open_order_feed_page()
        count_2 = order_feed_page.get_quantity_of_orders()
        assert count_1 < count_2

    @allure.title('Проверка увеличения числа на счетчике ежедневного количества выполненных заказов')
    def test_changes_counter_daily_orders_success(self, driver, auth_to_account):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        auth_to_account()
        main_page.click_header_feed_button()
        count_1 = order_feed_page.get_daily_quantity_of_orders()
        main_page.create_order_in_main()
        order_feed_page.open_order_feed_page()
        count_2 = order_feed_page.get_daily_quantity_of_orders()
        assert count_1 < count_2

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    def test_new_order_in_progress_success(self, driver, auth_to_account):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        auth_to_account()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        new_order_id = main_page.get_number_of_order_in_modal_confirmation()
        main_page.click_on_button_close_confirmation_modal()
        main_page.click_header_feed_button()
        assert order_feed_page.get_order_number_in_feed_progress_section() == f'0{new_order_id}'