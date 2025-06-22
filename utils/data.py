TEST_USER = {
    "email": "test_user@example.com",
    "password": "secure_password123"
}

# Дополнительные функции генерации данных (если нужны)
import random
import string

def generate_email():
    """Генерирует случайный email"""
    return f"test_{random_string(7)}@example.com"

def generate_password(length=10):
    """Генерирует случайный пароль"""
    return random_string(length)

def random_string(length):
    """Генерирует случайную строку заданной длины"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))