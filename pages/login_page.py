from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://stellarburgers.nomoreparties.site/login"
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    def __init__(self, browser):  # Изменено driver → browser
        self.browser = browser  # Сохраняем как browser
        self.wait = WebDriverWait(browser, 10)  # Используем browser

    def open(self):
        self.browser.get(self.URL)  # Используем self.browser
        # Добавим ожидание загрузки страницы
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))

    def login(self, email, password):
        # Используем константы локаторов
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