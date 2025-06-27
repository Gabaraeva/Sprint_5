from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import PERSONAL_ACCOUNT_URL, LOGIN_PAGE_URL, MAIN_PAGE_URL


class TestPersonalAccount:
    """Тесты для функциональности личного кабинета"""

    def test_go_to_personal_account(self, browser, authorized_user):
        """Проверка перехода в личный кабинет"""
        main_page = MainPage(browser)
        main_page.click_personal_account_button()

        # Явное ожидание загрузки страницы профиля
        WebDriverWait(browser, 10).until(
            EC.url_contains("/account/profile")
        )

        # Проверяем, что открылась страница профиля
        assert "account/profile" in browser.current_url, "Не удалось перейти в личный кабинет"

    def test_go_from_personal_account_to_constructor(self, browser, authorized_user):
        """Проверка перехода из ЛК в конструктор"""
        # Переходим в личный кабинет
        browser.get(PERSONAL_ACCOUNT_URL)

        # Кликаем на "Конструктор"
        browser.find_element(By.XPATH, "//p[text()='Конструктор']").click()

        # Проверяем переход на главную страницу
        WebDriverWait(browser, 10).until(
            EC.url_to_be(MAIN_PAGE_URL)
        )

        # Проверяем наличие кнопки заказа
        main_page = MainPage(browser)
        main_page.should_be_order_button()

    def test_go_from_personal_account_via_logo(self, browser, authorized_user):
        """Проверка перехода через логотип"""
        # Переходим в личный кабинет
        browser.get(PERSONAL_ACCOUNT_URL)

        # Кликаем на логотип
        browser.find_element(By.XPATH, "//div[contains(@class, 'logo')]").click()

        # Проверяем переход на главную страницу
        WebDriverWait(browser, 10).until(
            EC.url_to_be(MAIN_PAGE_URL)
        )

        # Проверяем наличие кнопки заказа
        main_page = MainPage(browser)
        main_page.should_be_order_button()

    def test_logout(self, browser, authorized_user):
        """Проверка выхода из аккаунта"""
        # Переходим в личный кабинет
        browser.get(PERSONAL_ACCOUNT_URL)

        # Кликаем "Выход"
        browser.find_element(By.XPATH, "//button[text()='Выход']").click()

        # Проверяем переход на страницу входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(LOGIN_PAGE_URL)
        )

        # Проверяем наличие формы входа
        login_page = LoginPage(browser)
        login_page.should_be_login_form()