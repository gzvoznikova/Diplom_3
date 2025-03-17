from locators.order_feed_page_locators import OrderFeedPageLocators
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
import allure
from urls import Urls
from selenium.webdriver.common.by import By


class OrderFeedPage(BasePage, MainPage):

    @allure.step("Открыть страницу 'Лента заказов'")
    def open_order_feed_page(self):
        self.open_url(Urls.order_feed_url)

    @allure.step('Подождать прогрузки карточки заказа')
    def wait_visibility_of_order_card(self):
        self.wait_visibility_of_element(OrderFeedPageLocators.order_card)

    @allure.step('Получить текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(OrderFeedPageLocators.order_card_title)

    @allure.step('Получить текст заголовка раздела заказов')
    def get_text_on_title_of_orders_list(self):
        return self.get_text_on_element(OrderFeedPageLocators.title_of_orders_feed)

    @allure.step('Кликнуть по первому (последнему) заказу в ленте')
    def click_on_order_card(self):
        self.wait_time()
        self.wait_visibility_of_element(OrderFeedPageLocators.order_in_feed)
        self.click_on_element(OrderFeedPageLocators.order_in_feed)

    @allure.step('Получить текст заголовка окна с деталями заказа')
    def get_text_on_title_of_modal_order(self):
        return self.get_text_on_element(OrderFeedPageLocators.title_of_modal_order)

    @allure.step('Получить количество заказов, выполненных за все время')
    def get_quantity_of_orders(self):
        self.find_element_with_wait(OrderFeedPageLocators.quantity_of_orders)
        return self.get_text_on_element(OrderFeedPageLocators.quantity_of_orders)

    @allure.step('Получить количество заказов, выполненных за сегодня')
    def get_daily_quantity_of_orders(self):
        self.wait_time()
        self.find_element_with_wait(OrderFeedPageLocators.daily_quantity_of_orders)
        return self.get_text_on_element(OrderFeedPageLocators.daily_quantity_of_orders)

    @allure.step('Получить номер последнего заказа в разделе "В работе"')
    def get_order_number_in_feed_progress_section(self):
        self.wait_time()
        return self.get_text_on_element(OrderFeedPageLocators.number_of_order_in_progress)

    @allure.step("Получить номер последнего заказа из История заказов")
    def get_last_order_history(self):
        return self.find_all_elements(OrderFeedPageLocators.last_order_number)[-1].text

    @allure.step("Проверить существование последнего номера заказа в Ленте заказов")
    def get_check_number_order(self, last_order):
        return self.find_all_elements((By.XPATH,
                                            f'//*[contains(@class,"rderHistory_textBox__")]//*[contains(@class,"text_type_digits-default") and contains(text(),"{last_order}")]'))




