import pytest


def division(a, b, h):  # Функция division принимает два аргумента
    return a / b * h


print('division_1 = ', (int(division(30, -3, - 10))))


def division_2(a, b, v):
    return a / b * v


print('division_2 = ', division_2(6, 10, 2))


def division_3(sex, sox, sax):
    return sex / sox * sax


print('division_3 = ', (int(division_3(10, 2, 5))))


def division_4(start, middle):
    return int(start + middle)


print('division_4 = {}', (int(division_4(10, 12))))
