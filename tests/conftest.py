import pytest
import random
import string
from api import CourierPage


@pytest.fixture
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    len_random = 100
    login = generate_random_string(len_random)
    password = generate_random_string(len_random)
    first_name = generate_random_string(len_random)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # тела запроса для регистрации
    return payload

@pytest.fixture
def valid_log_in_payload(register_new_courier_and_return_login_password):
    CourierPage.create_courier(register_new_courier_and_return_login_password)
    login_payload = {
        "login": register_new_courier_and_return_login_password["login"],
        "password": register_new_courier_and_return_login_password["password"],
    }
    return login_payload