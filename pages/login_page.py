from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import LOGIN_PAGE_URL  # Импорт из нового файла


class LoginPage:
    URL = LOGIN_PAGE_URL  # Используем импортированный URL

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.browser.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))

    def login(self, email, password):
        email_input = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    def click_password_recovery_link(self):
        link = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_RECOVERY_LINK))
        link.click()


    def should_be_login_form(self):
            """Проверяем наличие элементов формы входа"""
            self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
            self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
            self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
