"""
Создание веб клиента для работы с inari с реализацией метода GET
который запрашивал по указанному урлу нужные данные

Проверка данных у найденного урла:
res = requests.get('https://api.inari.pro/v3/catalog/public/goods/22376/stock-cities')
print(res.text)

https://api.inari.pro - это доменное имя URL - идентификация ресурса
/v3/catalog/public/goods/22376/stock-cities - эндпоинт или хвост URI - идентификатор внутри какого то ресурса

Второй пример с нужными параметрами

res = requests.get('https://queuev4.vk.com/im0721?act=a_check&key=7c8db7dafc9fddbd313f2df21e9c2be03efff5e0f218fa3dcae355a5a141e48c&id=13312721&ts=47043058&wait=30')
print(res.text)

"""

import requests
import json
from datetime import datetime


class Inari:
    def __init__(self, url):  # Создаем функцию с методом init, с базовым url на который мы будем стучаться
        self.url = url

    def get_inari_request(self, order_id):  # Создание метода, который будет забирать данные из указанного места
        resp = requests.get(f'{self.url}/v3/catalog/public/goods/{order_id}/stock-cities')
        json_data = json.loads(resp.text)
        return json_data

    def get_general_sum(self, order_id):
        json_data = self.get_inari_request(order_id)
        positionCount = json_data['allStocksPositions']['positionCount']
        cityId = json_data['byCity']['cityId']
        count = json_data['byCity']['count']
        return datetime.fromtimestamp(positionCount - cityId - count)


base_url_inari = Inari('https://api.inari.pro')
base_url_inari.get_inari_request(22376)
print(base_url_inari.get_inari_request(22376))
#print(base_url_inari.get_general_sum(22376))  # Ошибка в данной строке не может видимо посчитать время


class VK:
    def __init__(self, url):  # Создаем функцию с методом init, с базовым url на который мы будем стучаться
        self.url = url

    def get_vk_request(self, order_id):  # Создание метода, который будет забирать данные из указанного места
        resp = requests.get(f'{self.url}/im0721?act=a_check&key=7c8db7dafc9fddbd313f2df21e9c2be03efff5e0f218fa3dcae355a5a141e48c&id={order_id}&ts=47043058&wait=30')
        json_data = json.loads(resp.text)
        return json_data

    def get_general_sum(self, order_id):
        json_data = self.get_vk_request(order_id)
        failed_json = json_data['failed']
        err_json = json_data['err']
        return datetime.fromtimestamp(failed_json - err_json)


base_url_vk = VK('https://queuev4.vk.com')
base_url_vk.get_vk_request(13312721)
print(base_url_vk.get_vk_request(13312721))
#print(base_url_vk.get_general_sum(13312721))  # Ошибка в данной строке не может видимо посчитать время


