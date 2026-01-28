import allure
from order_metods import MetodsOrders
import pytest
from data import TextConstants


class TestGetListOrders:
    @allure.title('Проверка успешного получения списка заказов')
    @allure.description('Получение общего списка заказов')
    def test_get_orders_list_success(self):
        
        responce  = MetodsOrders.list_order()
        assert responce.status_code == 200
        assert TextConstants.WORD_ORDERS_IN_RESPONSE in responce.text