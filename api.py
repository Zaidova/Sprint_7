import requests
import allure
import url


class CourierPage:

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(payload):
        response = requests.post(url.COURIER_URL, data=payload, timeout=20)
        return response

    @staticmethod
    @allure.step("Авторизация курьера")
    def log_in_courier(payload):
        response = requests.post(url.LOGIN_COURIER_URL, data=payload, timeout=20)
        return response

class OrderPage:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(url.ORDER_URL, data=payload, timeout=20)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_all_orders():
        response = requests.get(url.ORDER_URL, timeout=60)
        return response