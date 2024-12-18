import allure
from data import *
from tests.conftest import *


class TestLoginCourier:

    @allure.title('Успешная автоизация курьера')
    def test_login_courier_success(self,valid_log_in_payload):
        response = CourierPage.log_in_courier(valid_log_in_payload)
        assert response.status_code == 200
        assert response.json()["id"]

    @pytest.mark.parametrize('remove_fields', ['login', 'password'])
    @allure.title('Заполнение обязательных полей при авторизации, поле {remove_fields}')
    def test_remove_fields_login_courier_error_missing(self,valid_log_in_payload, remove_fields):
        valid_log_in_payload.pop(remove_fields)
        response = CourierPage.log_in_courier(valid_log_in_payload)
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MISSING_FIELDS_LOG_IN_COURIER

    @pytest.mark.parametrize('invalid_data_fields', ['login', 'password'])
    @allure.title('Ошибка при непрравильно указанном поле {invalid_data_fields}')
    def test_invalid_data_login_courier_error_not_found(self,valid_log_in_payload, invalid_data_fields):
        valid_log_in_payload[invalid_data_fields] = 'неверный логин/пароль'
        response = CourierPage.log_in_courier(valid_log_in_payload)
        assert response.status_code == 404
        assert response.json()["message"] == ERROR_NOT_FOUND