import requests
import random
import string
from urls import Urls
from faker import Faker


class Generation:
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_courier_data():
        login = Generation.generate_random_string(10)
        password = Generation.generate_random_string(10)
        first_name = Generation.generate_random_string(10)
        payload = {
        "login": login,
        "password": password,
        "firstName": first_name
        }
        return payload


    def choose_color(color=''):
      faker = Faker('ru_RU')
      metro_station_list = [
        'Бульвар Рокоссовского','Преображенская площадь','Сокольники','Войковская',
        'Комсомольская','Красные Ворота','Чистые пруды','Лубянка',
        'Охотный Ряд','Библиотека имени Ленина','Кропоткинская','Парк культуры',
        'Фрунзенская','Воробьёвы горы','Университет','Юго-Западная',
        'Тропарёво','Саларьево'
      ]
      if isinstance(color, str):
        color = [color] if color else []

      data =  {
      "firstName": faker.first_name(),
      "lastName": faker.last_name(),
      "address": f'улица {faker.street_name()}, дом {faker.random_int(min=1, max=1000)}, кв. {faker.random_int(min=1, max=1000)}',
      "metroStation": random.choice(metro_station_list),
      "phone": f'+7{faker.random_int(min=0000000000, max=999999999)}',
      "rentTime": faker.random_int(min=1, max=5),
      "deliveryDate": faker.date_between(start_date='today', end_date='+5d').isoformat(),
      "comment": faker.word(),
      "color": color
      }
      return data
    
c= Generation
print(c.choose_color())
