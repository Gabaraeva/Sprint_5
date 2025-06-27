from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.password_recovery_page import PasswordRecoveryPage
from utils.data import generate_email, generate_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_login_via_main_page_button(self, browser):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        # Регистрация тестового пользователя
        email = generate_email()
        password = generate_password()
        registration_page = RegistrationPage(browser)
        registration_page.register("Тестовый Пользователь", email, password)

        # Выход из системы
        main_page = MainPage(browser)
        main_page.click_personal_account_button()

        # Явное ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_contains("/login"))

        # Вход
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(email, password)

        # Проверка успешного входа
        main_page.should_be_order_button()

    def test_login_via_personal_account_button(self, browser):
        """Вход через кнопку 'Личный кабинет'"""
        # Регистрация тестового пользователя
        email = generate_email()
        password = generate_password()
        registration_page = RegistrationPage(browser)
        registration_page.register("Тестовый Пользователь", email, password)

        # Выход из системы
        main_page = MainPage(browser)
        main_page.click_personal_account_button()

        # Явное ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_contains("/login"))

        # Вход
        main_page.open()
        main_page.click_personal_account_button()

        login_page = LoginPage(browser)
        login_page.login(email, password)

        # Проверка успешного входа
        main_page.should_be_order_button()

    def test_login_via_registration_form(self, browser):
        """Вход через кнопку в форме регистрации"""
        # Переход на страницу регистрации
        registration_page = RegistrationPage(browser)
        registration_page.open()

        # Клик по кнопке "Войти"
        registration_page.click_login_link()

        # Явное ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_contains("/login"))

        # Создаем пользователя
        email = generate_email()
        password = generate_password()
        registration_page.register("Тестовый Пользователь", email, password)

        # Выход (для чистоты теста)
        main_page = MainPage(browser)
        main_page.click_personal_account_button()

        # Явное ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_contains("/login"))

        # Повторный вход через форму регистрации
        registration_page.open()
        registration_page.click_login_link()

        # Явное ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_contains("/login"))

        login_page = LoginPage(browser)
        login_page.login(email, password)

        # Проверка успешного входа
        main_page.should_be_order_button()

    def test_login_via_password_recovery(self, browser):
        """Вход через кнопку в форме восстановления пароля"""
        # Регистрация тестового пользователя
        email = generate_email()
        password = generate_password()
        registration_page = RegistrationPage(browser)
        registration_page.register("Тестовый Пользователь", email, password)

        # Выход из системы
        main_page = MainPage(browser)
        main_page.click_personal_account_button()

        # Явное ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_contains("/login"))

        # Переход на страницу восстановления пароля
        login_page = LoginPage(browser)
        login_page.open()
        login_page.click_password_recovery_link()

        # Явное ожидание перехода на страницу восстановления
        WebDriverWait(browser, 10).until(EC.url_contains("/forgot-password"))

        # Клик по кнопке "Войти"
        recovery_page = PasswordRecoveryPage(browser)
        recovery_page.click_login_link()

        # Явное ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_contains("/login"))

        # Вход
        login_page.login(email, password)

        # Проверка успешного входа
        main_page = MainPage(browser)
        main_page.should_be_order_button()