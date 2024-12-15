import allure
import pytest

from api import OrderPage
from data import *


class TestCreateOrderColors:

    @pytest.mark.parametrize(
        "colors",
        [["BLACK"], ["GREY"], ["BLACK", "GREY"], None],
    )
    @allure.title('Создание заказа с различными цветами')
    def test_create_order_with_colors(self, colors):
        payload = ORDER_PAYLOAD.copy()
        payload["color"] = colors
        response  = OrderPage.create_order(ORDER_PAYLOAD)
        assert response.status_code == 201 and response.json()["track"]


    @allure.title('Создание заказа без выбора цвета')
    def test_create_order_without_field_color(self):
        response  = OrderPage.create_order(ORDER_PAYLOAD)
        assert response.status_code == 201 and response.json()["track"]