import allure
from api import OrderPage


class TestGETOrder:

    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    def test_get_courier_id_orders_list_all_orders(self):
        response  = OrderPage.get_all_orders()
        assert response.status_code == 200 and len(response.json()["orders"]) > 0