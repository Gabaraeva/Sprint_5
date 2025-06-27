from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
from locators.registration_page_locators import RegistrationPageLocators
from urls import MAIN_PAGE_URL
from utils.data import generate_email, generate_password, generate_short_password


class TestRegistration:
    """Тесты для функциональности регистрации"""

    def test_successful_user_registration(self, browser):
        """
        Тест успешной регистрации пользователя
        """
        # Инициализация страницы регистрации
        registration_page = RegistrationPage(browser)
        registration_page.open()

        # Проверяем, что открылась страница регистрации
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_TITLE)
        )

        # Генерируем тестовые данные
        name = "Тестовый Пользователь"
        email = generate_email()
        password = generate_password()

        # Заполняем форму регистрации
        registration_page.register(name, email, password)

        # Проверяем переход на главную страницу после регистрации
        WebDriverWait(browser, 10).until(
            EC.url_to_be(MAIN_PAGE_URL)
        )

        # Проверяем наличие кнопки "Оформить заказ"
        order_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после регистрации"

    def test_invalid_password_error(self, browser):
        """
        Тест ошибки при некорректном пароле
        """
        # Инициализация страницы регистрации
        registration_page = RegistrationPage(browser)
        registration_page.open()

        # Проверяем, что открылась страница регистрации
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_TITLE)
        )

        # Генерируем тестовые данные с коротким паролем
        name = "Тестовый Пользователь"
        email = generate_email()
        password = generate_short_password()  # Пароль из 5 символов

        # Заполняем форму регистрации
        registration_page.register(name, email, password)

        # Проверяем сообщение об ошибке
        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )
        assert "Некорректный пароль" in error_message.text, \
            f"Ожидалась ошибка 'Некорректный пароль', получено: '{error_message.text}'"