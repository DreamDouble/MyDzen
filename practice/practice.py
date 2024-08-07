def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage()

"""Здесь мы создаём декоратор, замеряющий время выполнения функции. 
Далее мы используем его на функции, которая делает GET-запрос к главной странице Google. 
Чтобы измерить скорость, мы сначала сохраняем время перед выполнением обёрнутой функции, выполняем её, 
снова сохраняем текущее время и вычитаем из него начальное.
Запомнить!
Декоратор принимает функцию в качестве аргумента и возвращает функцию."""