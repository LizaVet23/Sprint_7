import allure
from courier_metods import MetodsCourier
import pytest
from data import TextConstants


class TestCreatingCouriers:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Создание курьера с заполнеными обязательными полями')
    def test_creating_courier_success(self,courier_create_data):
        with allure.step('Создание курьера'):
            create = MetodsCourier.creaite_courier(courier_create_data)
        assert create.status_code == 201
        assert create.text == TextConstants.SUCCESS_MESSAGE
        

    @allure.title('Проверка невозможности создать двух одинаковых курьеров')
    @allure.description('Создание второго курьера с одинаковыми данными')
    def test_creating_double_courier_conflict(self,courier_create_data):
        with allure.step('Создание курьера'):
            payload = courier_create_data
            create = MetodsCourier.creaite_courier(payload)
            with allure.step('Создание второго курьера'):
                if create.status_code == 201 and create.text == TextConstants.SUCCESS_MESSAGE:
                    create2 = MetodsCourier.creaite_courier(payload)
        assert create2.status_code == 409
        assert create2.text == TextConstants.LOG_ERROR_MESSAGE

    @allure.title('Проверка невозможности создать курьера без обязательных данных')
    @pytest.mark.parametrize('parameter',[('login'),('password')] )
    def test_impossible_create_courier_without_required_data(self,courier_create_data, parameter):
        allure.dynamic.description(f'Проверка создания курьера без обязательного параметра - {parameter}')
        payload = courier_create_data
        payload.pop(parameter)
        create = MetodsCourier.creaite_courier(payload)
        assert create.status_code == 400
        assert create.text == TextConstants.INSUFFICIENT_DATA_TO_CREATE_MESSAGE


    