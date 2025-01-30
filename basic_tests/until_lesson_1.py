import pytest


def division_1(a, b, h):  # Функция division принимает три аргумента
    return a / b * h  # возвращаем результат a / b * h


# Будем скармливать нашей функции division какие-то значения
print('division_1 = ', (int(division_1(30, -3, - 10))))


def division_2(a, b, v):
    return a / b * v


print('division_2 = ', division_2(6, 10, 2))


def division_3(sex, sox, sax):
    return sex / sox * sax


print('division_3 = -_-', (int(division_3(10, 2, 5))))


def division_4(start, middle):
    return int(start + middle)


print('division_4 = {}', (int(division_4(10, 12))))


def division_5(hot, dog, hot_dog):  # Создал функцию, передал 3 аргумента
    return hot + dog * hot_dog


print('division_5 = {}', (float(division_5(5, 40, 12))))  # float ставит точку в конце результата
