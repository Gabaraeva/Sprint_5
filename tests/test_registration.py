from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
from locators.registration_page_locators import RegistrationPageLocators
from urls import MAIN_PAGE_URL  # Удален неиспользуемый импорт REGISTRATION_PAGE_URL


def test_successful_user_registration(browser):
    """
    Тест успешной регистрации пользователя
    """
    # Инициализация страницы регистрации
    registration_page = RegistrationPage(browser)

    # Открываем страницу регистрации (URL используется внутри класса)
    registration_page.open()

    # Проверяем, что открылась именно страница регистрации
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_TITLE)
    )

    # Заполняем форму регистрации
    registration_page.register(
        name="Тестовый Пользователь",
        email="test_user@example.com",
        password="Password123"
    )

    # Проверяем переход на главную страницу после регистрации
    WebDriverWait(browser, 10).until(
        EC.url_to_be(MAIN_PAGE_URL)
    )

    # Проверяем наличие кнопки "Оформить заказ" на главной странице
    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.ORDER_BUTTON)
    )
    assert order_button.is_displayed(), "После регистрации не отображается кнопка 'Оформить заказ'"