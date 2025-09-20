import pytest
from courier_metods import MetodsCourier
from order_metods import MetodsOrders
from helpers import Generation


@pytest.fixture(scope="function")
def courier_create_data():
    try:
        payload = Generation.generate_random_courier_data()
        login = payload['login']
        password = payload['password']
        first_name = payload['firstName']
        yield payload
        courier_id = MetodsCourier.get_courier_id(login,password)
        MetodsCourier.delete_courier(courier_id)
    except KeyError as e:
        print(f"Произошла ошибка KeyError: {e}")
    except Exception as e:
       print(f"Произошла ошибка: {e}")


@pytest.fixture(scope="function")
def courier_login():
    try:
        payload = Generation.generate_random_courier_data()
        login = payload['login']
        password = payload['password']
        first_name = payload['firstName']
        create = MetodsCourier.creaite_courier(payload)
        log = {
            "login": login,
            "password": password
        }
        yield log
        courier_id = MetodsCourier.get_courier_id(login,password)
        MetodsCourier.delete_courier(courier_id)
    except Exception as e:
       print(f"Произошла ошибка: {e}")


@pytest.fixture(scope="function")
def clean_order():
    try:
        track_number = None
    
        def _clean_order(track):
           nonlocal track_number
           track_number = track
    
        def teardown():
            if track_number:
                MetodsOrders.clean_order(track_number)
                          
        yield _clean_order
        teardown()
    except Exception as e:
       print(f"Произошла ошибка: {e}")

