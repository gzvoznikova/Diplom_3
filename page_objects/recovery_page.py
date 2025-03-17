from page_objects.base_page import BasePage
from locators.recovery_page_locators import RecoveryPassLocators
from data import DataUser
import allure


class RecoveryPassPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def navigate_to_recovery_passwd_page(self):
        self.wait_visibility_of_element(RecoveryPassLocators.button_forgot_password)
        self.click_on_element(RecoveryPassLocators.button_forgot_password)

    @allure.step('Проверить отображение поля email')
    def check_displaying_of_input_email(self):
        return self.check_displaying_of_element(RecoveryPassLocators.input_email)

    @allure.step('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(RecoveryPassLocators.input_email)
        email = DataUser.email
        self.send_keys_to_input(RecoveryPassLocators.input_email, email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(RecoveryPassLocators.button_recover)
        self.click_on_element(RecoveryPassLocators.button_recover)

    @allure.step('Проверить отображение поля password')
    def check_displaying_of_input_password(self):
        self.wait_visibility_of_element(RecoveryPassLocators.input_password)
        return self.check_displaying_of_element(RecoveryPassLocators.input_password)

    @allure.step('Ввести password')
    def send_password(self):
        self.wait_visibility_of_element(RecoveryPassLocators.input_password)
        passwd = DataUser.password
        self.send_keys_to_input(RecoveryPassLocators.input_password, passwd)

    @allure.step('Кликнуть на иконку глаза в поле ввода пароля')
    def click_on_eye_icon(self):
        self.wait_visibility_of_element(RecoveryPassLocators.eye_icon)
        self.click_on_element(RecoveryPassLocators.eye_icon)

    @allure.step("Проверка активации поля пароля")
    def is_password_field_active(self):
        return self.is_element_active(RecoveryPassLocators.value_password_is_visible)

    @allure.step("Клик по кнопке 'Войти'")
    def click_button_login_in_auth(self):
        self.click_on_element(RecoveryPassLocators.button_login_in_auth)
