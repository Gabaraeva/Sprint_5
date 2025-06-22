# conftest.py
import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.data import TEST_USER

# Добавляем корень проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def authorized_user(browser):
    """Фикстура для авторизованного пользователя"""
    from pages.main_page import MainPage
    from pages.login_page import LoginPage

    main_page = MainPage(browser)
    main_page.open()
    main_page.click_login_button()

    login_page = LoginPage(browser)
    login_page.login(TEST_USER['email'], TEST_USER['password'])

    return TEST_USER