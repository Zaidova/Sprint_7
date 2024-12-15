import pytest
import allure
from data import *
from api import CourierPage


class TestCreateCourier:

    @allure.title('Создание нового курьерa')
    def test_create_new_courier(self, register_new_courier_and_return_login_password):
        response = CourierPage.create_courier(register_new_courier_and_return_login_password)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_courier_duplicate(self, register_new_courier_and_return_login_password):
        CourierPage.create_courier(register_new_courier_and_return_login_password)
        response_courier_duplicate = CourierPage.create_courier(register_new_courier_and_return_login_password)
        assert response_courier_duplicate.status_code == 409 and response_courier_duplicate.json()["message"] == ERROR_LOGIN_DUPLICATE

    @pytest.mark.parametrize('remove_fields', ['login', 'password'])
    @allure.title('Создание курьера без поля {remove_fields}')
    def test_create_remove_fields_courier(self, register_new_courier_and_return_login_password, remove_fields):
        register_new_courier_and_return_login_password.pop(remove_fields)
        response  = CourierPage.create_courier(register_new_courier_and_return_login_password)
        assert response.status_code == 400 and response.json()["message"] == ERROR_MISSING_FIELDS_CREATE_COURIER