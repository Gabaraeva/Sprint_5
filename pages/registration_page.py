from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    # Локаторы
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Конструктор класса (добавьте этот метод)
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)  # Инициализация ожидания

    def open(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/register")

        # Ожидание загрузки страницы
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[text()='Регистрация']")
        ))

    def register(self, name, email, password):
        # Используем wait для всех элементов
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()

    def click_login_link(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()
