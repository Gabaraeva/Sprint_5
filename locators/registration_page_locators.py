from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # Существующие локаторы
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")

    # Добавим локаторы для проверки успешной регистрации
    REGISTRATION_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

