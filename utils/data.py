TEST_USER = {
    "email": "test_user@example.com",
    "password": "secure_password123"
}

# Функции генерации данных
import random
import string

def generate_email():
    """Генерирует случайный email"""
    return f"test_{random_string(7)}@example.com"

def generate_password(length=10):
    """Генерирует случайный пароль заданной длины"""
    return random_string(length)

def generate_short_password():
    """Генерирует короткий пароль (5 символов) для теста ошибок"""
    return generate_password(5)  # Используем существующую функцию с длиной 5

def random_string(length):
    """Генерирует случайную строку заданной длины"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))