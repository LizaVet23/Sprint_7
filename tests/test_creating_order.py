import allure
from order_metods import MetodsOrders
import pytest
from helpers import Generation
from data import TextConstants


class TestCreatingOrders:
    @allure.title('Проверка успешного создания заказа при различной вариации передачи параметра color')
    @pytest.mark.parametrize('color', [['BLACK'],['GREY'], [''],['BLACK', 'GREY']] )
    def test_creating_order_with_color_success(self,clean_order, color ):
        allure.dynamic.description(f'Проверка создания заказа при передаче параметра color - {color}')
        with allure.step('Создание заказа'):
            create, track_number = MetodsOrders.create_order(Generation.choose_color(color))
            clean_order(track_number)
            
        assert create.status_code == 201
        assert TextConstants.WORD_TRACK_IN_RESPONSE in create.text