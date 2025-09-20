import allure
import requests
from urls import Urls


class MetodsCourier:

    @staticmethod
    @allure.step('Создание курьера')
    def creaite_courier(payload):
        return requests.post(f'{Urls.MAIN_SITE}{Urls.CREATE_COURIER}', data=payload)
         
         
    @staticmethod
    @allure.step('Авторизация курьера в системе')
    def login_courier(payload):
        return requests.post(f'{Urls.MAIN_SITE}{Urls.COURIER_LOGIN}', data=payload)


    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(id):
        return requests.delete(f'{Urls.MAIN_SITE}{Urls.DELETE_COURIER}{id}', data={f'"id":"{id}"'})
    

    @staticmethod
    @allure.step('Получение id курьера')
    def get_courier_id(login,password):
        response = requests.post(f'{Urls.MAIN_SITE}{Urls.COURIER_LOGIN}', data={
            "login": login,
            "password": password
        })
        r = response.json()
        id = r['id']
        return id