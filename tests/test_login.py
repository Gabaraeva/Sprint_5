from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage  # Добавлен импорт
from utils.data import generate_email, generate_password
import time


def test_login_via_main_page_button(browser):
    """Вход через кнопку 'Войти в аккаунт' на главной"""
    # Регистрация тестового пользователя
    email = generate_email()
    password = generate_password()
    registration_page = RegistrationPage(browser)
    registration_page.register("Тестовый Пользователь", email, password)

    # Выход из системы
    main_page = MainPage(browser)
    main_page.click_personal_account_button()
    personal_account_page = PersonalAccountPage(browser)
    personal_account_page.logout()
    time.sleep(1)  # Ожидание выхода

    # Вход
    main_page.open()
    main_page.click_login_button()

    login_page = LoginPage(browser)
    login_page.login(email, password)

    # Проверка успешного входа
    main_page.should_be_order_button()


def test_login_via_personal_account_button(browser):
    """Вход через кнопку 'Личный кабинет'"""
    # Регистрация тестового пользователя
    email = generate_email()
    password = generate_password()
    registration_page = RegistrationPage(browser)
    registration_page.register("Тестовый Пользователь", email, password)

    # Выход из системы
    main_page = MainPage(browser)
    main_page.click_personal_account_button()
    personal_account_page = PersonalAccountPage(browser)
    personal_account_page.logout()
    time.sleep(1)  # Ожидание выхода

    # Вход
    main_page.open()
    main_page.click_personal_account_button()

    login_page = LoginPage(browser)
    login_page.login(email, password)

    # Проверка успешного входа
    main_page.should_be_order_button()


def test_login_via_registration_form(browser):
    """Вход через кнопку в форме регистрации"""
    # Переход на страницу регистрации
    registration_page = RegistrationPage(browser)
    registration_page.open()

    # Клик по кнопке "Войти"
    registration_page.click_login_link()

    # Создаем пользователя
    email = generate_email()
    password = generate_password()
    registration_page.register("Тестовый Пользователь", email, password)

    # Выход (для чистоты теста)
    main_page = MainPage(browser)
    main_page.click_personal_account_button()
    personal_account_page = PersonalAccountPage(browser)
    personal_account_page.logout()
    time.sleep(1)  # Ожидание выхода

    # Повторный вход через форму регистрации
    registration_page.open()
    registration_page.click_login_link()

    login_page = LoginPage(browser)
    login_page.login(email, password)

    # Проверка успешного входа
    main_page.should_be_order_button()




def test_login_via_password_recovery(browser):
    """Вход через кнопку в форме восстановления пароля"""
    # Регистрация тестового пользователя
    email = generate_email()
    password = generate_password()
    registration_page = RegistrationPage(browser)
    registration_page.register("Тестовый Пользователь", email, password)

    # Выход из системы
    main_page = MainPage(browser)
    main_page.click_personal_account_button()
    personal_account_page = PersonalAccountPage(browser)
    personal_account_page.logout()
    time.sleep(1)  # Ожидание выхода

    # Переход на страницу восстановления пароля
    login_page = LoginPage(browser)
    login_page.open()
    login_page.click_password_recovery_link()

    # Клик по кнопке "Войти"
    recovery_page = PasswordRecoveryPage(browser)
    recovery_page.click_login_link()

    # Вход
    login_page.login(email, password)

    # Проверка успешного входа
    main_page = MainPage(browser)
    main_page.should_be_order_button()

