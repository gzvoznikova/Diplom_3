from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ожидание загрузки страницы: {url}")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        target = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Ждать исчезновения элемента')
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 40).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Проверка активности элемента")
    def is_element_active(self, locator, active_class="input_status_active"):
        element = self.driver.find_element(*locator)
        return self.wait.until(lambda driver: active_class in element.get_attribute("class"))

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Перенос элемента')
    def drag_and_drop(self, element, target):
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
            """,
            element,
            target
        )

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Получить кликабельный элемент')
    def find_all_elements(self, locator):
        self.check_element_is_clickable(locator)
        return self.driver.find_elements(*locator)

    @allure.step("Проверка, что текст '{text}' присутствует в списке элементов")
    def is_text_in_elements(self, locator, text):
        elements_text = self.get_text_on_element(locator)
        return any(text == element_text.strip() for element_text in elements_text)

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 5).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Подождать смену текста на элементе')
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.
                                                        text_to_be_present_in_element(locator, value))

    @allure.step("Проверка соответствия URL: {expected_url}")
    def is_current_url(self, expected_url):
        try:
            self.wait.until(EC.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False


