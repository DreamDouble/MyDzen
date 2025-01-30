import pytest  # библиотека, которая помогает тестировать код на python

from basic_tests.until_lesson_1 import division_1, division_2, division_3, division_4, division_5


class Test_the_division:

    def test_devision_true(self):
        assert division_1(30, -3, - 10) == 100  # Функция assert проверяет являеться ли наш результат значением true

    def test_devision_false(self):
        assert division_1(10, 2) == 2

    def test_division_true_2(self):
        assert division_2(6, 10, 2) == 1.2

    def test_division_false_2(self):
        assert division_2(3, 8, 30) == 120

    def test_division_true_3(self):
        assert division_5(5, 40, 12) == 485.0


"""Аналогичные тесты только через параметризацию
@pytest.mark.parametrize - специальный декоратор, которому сначала передается строка - (), далее переменные - sex, sax
которые прокидываем в нашу функцию, далее лист с картежами - 10, 2, 5, 25"""


@pytest.mark.parametrize('sex, sox, sax, super_sex', [(10, 2, 5, 25), (6, 10, 2, 1.2), (30, -3, - 10, 100)])
def test_division_all_true(sex, sox, sax, super_sex):
    assert division_3(sex, sox, sax) == super_sex


@pytest.mark.parametrize('hot, dog, hot_dog, super_hot_dog', [(5, 40, 12, 485.0)])
def test_division_hot_dog(hot, dog, hot_dog, super_hot_dog):
    assert division_5(hot, dog, hot_dog) == super_hot_dog


"""Негативные тесты"""


def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        assert division_3(10, 0, 0)


def test_division_type_error():
    with pytest.raises(TypeError):
        assert division_3(10, 8, '2')


"""Аналогичные негативные тесты только через параметризацию"""


@pytest.mark.parametrize('start, middle, end', [(ZeroDivisionError, 0, 10), (TypeError, 10, '2')])
def test_division_error(start, middle, end):
    with pytest.raises(start):  # Убедиться в том, что вызвано ожидаемое исключение, для этого юзаем функцию pytest.raises()
        assert division_4(middle, end)


"""Для себя, есть пакеты тестов как пример "tests" в нем есть разные поддиректории """
