from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL
import pytest


class TestConstructorSections:
    """Тесты разделов конструктора бургеров"""

    # Локаторы разделов
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/..")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/..")
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/..")

    # Локатор активного раздела
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    @pytest.fixture(autouse=True)
    def open_main_page(self, browser):
        """Фикстура: открывает главную страницу перед каждым тестом"""
        browser.get(MAIN_PAGE_URL)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(self.BUNS_SECTION)
        )

    def test_switch_to_buns_section(self, browser):
        """Тест переключения на раздел 'Булки'"""
        # Кликаем на раздел "Булки"
        browser.find_element(*self.BUNS_SECTION).click()

        # Проверяем активный раздел
        active_section = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(self.ACTIVE_SECTION)
        )
        assert "Булки" in active_section.text

        # Дополнительная проверка: видимость хотя бы одного элемента булки
        buns_items = browser.find_elements(By.XPATH, "//h2[text()='Булки']/following-sibling::ul//a")
        assert len(buns_items) > 0, "В разделе 'Булки' нет отображаемых элементов"

    def test_switch_to_sauces_section(self, browser):
        """Тест переключения на раздел 'Соусы'"""
        # Кликаем на раздел "Соусы"
        browser.find_element(*self.SAUCES_SECTION).click()

        # Проверяем активный раздел
        active_section = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(self.ACTIVE_SECTION)
        )
        assert "Соусы" in active_section.text

        # Проверяем элементы соусов
        sauces_items = browser.find_elements(By.XPATH, "//h2[text()='Соусы']/following-sibling::ul//a")
        assert len(sauces_items) > 0

    def test_switch_to_toppings_section(self, browser):
        """Тест переключения на раздел 'Начинки'"""
        # Кликаем на раздел "Начинки"
        browser.find_element(*self.TOPPINGS_SECTION).click()

        # Проверяем активный раздел
        active_section = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(self.ACTIVE_SECTION)
        )
        assert "Начинки" in active_section.text

        # Проверяем элементы начинок
        toppings_items = browser.find_elements(By.XPATH, "//h2[text()='Начинки']/following-sibling::ul//a")
        assert len(toppings_items) > 0