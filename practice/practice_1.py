"""
Практика работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
"""

import requests
import json

res = requests.get('https://queuev4.vk.com/im0721?act=a_check&key=7c8db7dafc9fddbd313f2df21e9c2be03efff5e0f218fa3dcae355a5a141e48c&id=13312721&ts=47043058&wait=30')
print(res.text)



