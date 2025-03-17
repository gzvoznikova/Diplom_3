from conftest import *
from page_objects.recovery_page import RecoveryPassPage
from page_objects.main_page import MainPage
import allure

class TestPasswdRecoveryPage:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_recovery_pass_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = RecoveryPassPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        assert recovery_page.check_displaying_of_input_email()

    @allure.title('Проверка восстановления пароля')
    def test_click_recovery_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = RecoveryPassPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        assert recovery_page.check_displaying_of_input_password()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_password_field_activation(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPassPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.click_on_recovery_button()
        main_page.wait_time()
        recovery_page.send_email()
        recovery_page.click_on_eye_icon()
        assert recovery_page.is_password_field_active()
