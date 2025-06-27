from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL  # Импортируем из urls.py

class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный кабинет']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(MAIN_PAGE_URL)  # Используем константу из urls.py

    def click_login_button(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def click_personal_account_button(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.PERSONAL_ACCOUNT_BUTTON)
        ).click()

    def should_be_order_button(self):
        # Исправленная строка (замена точки на скобку)
        assert WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.ORDER_BUTTON)
        ), "Кнопка 'Оформить заказ' не отображается"
