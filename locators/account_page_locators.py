from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Раздел "Профиль"
    profile = (By.XPATH, '//a[@href = "/account/profile"]')

    # Раздел "История заказов"
    order_history = (By.XPATH, "//a[contains(@href, '/account/order-history') and contains(@class, 'Account_link')]")

    # Кнопка "Выйти", логаут
    button_logout = (By.XPATH, '//button[@type = "button"]')

    # Кнопка "Зарегистрироваться"
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Описание раздела: "В этом разделе вы можете изменить свои персональные данные"
    description_of_section = (By.XPATH, '//p[contains(@class, "Account_text")]')

