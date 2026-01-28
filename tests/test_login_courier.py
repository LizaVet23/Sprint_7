import allure
from courier_metods import MetodsCourier
import pytest
from data import TextConstants, WrongData


class TestLoginCouriers:
    @allure.title('Проверка успешного входа курьера в систему')
    @allure.description('Вход существующего курьера с верным логином и паролем')
    def test_login_courier_success(self,courier_login):
        with allure.step('Вход курьера в систему'):
            log_courier = MetodsCourier.login_courier(courier_login)
        assert log_courier.status_code == 200
        assert TextConstants.WORD_ID_IN_RESPONSE in log_courier.text


    @allure.title('Проверка невозможности входа в систему курьера без обязательного параметра')
    @pytest.mark.parametrize('parameter',[('login'),('password')] )
    def test_login_without_obligatory_parametr_unsuccess(self,courier_login, parameter):
        allure.dynamic.description(f'Вход в систему  без обязательного параметра - {parameter}')
        payload = courier_login
        payload.pop(parameter)
        log_courier = MetodsCourier.login_courier(payload)
        assert log_courier.status_code == 400
        assert log_courier.text == TextConstants.INSUFFICIENT_LOGIN_INFORMATION_MESSAGE


    @allure.title('Проверка невозможности входа в систему курьера с неправильными данными для входа')
    @pytest.mark.parametrize('parameter, wrong_value',[('login', WrongData.login),('password', WrongData.password)] )
    def test_login_with_wrong_obligatory_parametr_unsuccess(self,courier_login, parameter, wrong_value):
        allure.dynamic.description(f'Вход в систему с неправильным параметром - {parameter}')
        payload = courier_login
        payload.update({parameter: wrong_value})
        log_courier = MetodsCourier.login_courier(payload)
        assert log_courier.status_code == 404
        assert log_courier.text == TextConstants.ACCOUNT_NOT_FOUND_MESSAGE