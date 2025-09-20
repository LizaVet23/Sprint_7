import allure
import requests
from urls import Urls


class MetodsOrders:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(payload):
        response =  requests.post(f'{Urls.MAIN_SITE}{Urls.CREATE_ORDER}', json=payload)
        r = response.json()
        track = r.get('track')
        return response, track 
    
    @staticmethod
    @allure.step('Отменить заказ')
    def clean_order(track):
        params =f'track={track}'
        r = requests.put(f'{Urls.MAIN_SITE}{Urls.CANCEL_ORDER}', params = params)
        return r
    
    @staticmethod
    @allure.step('Получение списка заказов')
    def list_order(params=None):
        return requests.get(f'{Urls.MAIN_SITE}{Urls.LIST_ORDER}',params = params)