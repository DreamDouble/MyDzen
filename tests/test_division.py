import pytest

from basic_tests.utils import division, division_2, division_3, division_4


class Test_the_division:

    def test_devision_true(self):
        assert division(30, -3, - 10) == 100  # Функция assert проверяет являться ли наш результат значением true

    def test_devision_false(self):
        assert division(10, 2) == 2

    def test_division_true_2(self):
        assert division_2(6, 10, 2) == 1.2

    def test_division_false_2(self):
        assert division_2(3, 8, 30) == 120


"""Аналогичные тесты только через параметризацию"""


@pytest.mark.parametrize('sex, sox, sax, super_sex', [(10, 2, 5, 25), (6, 10, 2, 1.2), (30, -3, - 10, 100)])
def test_division_all_true(sex, sox, sax, super_sex):
    assert division_3(sex, sox, sax) == super_sex

"""Негативные тесты"""
def test_division_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert division_3(10, 0, 0)


def test_division_type_error():
    with pytest.raises(TypeError):
        assert division_3(10, 8, '2')


"""Аналогичные тесты только через параметризацию"""
@pytest.mark.parametrize('start, middle, end', [(ZeroDivisionError, 0, 10), (TypeError, 10, '2')])
def test_division_error(start, middle, end):
    with pytest.raises(start):  # Чтобы убедиться в том, что вызвано ожидаемое исключение, нужно использовать функцию pytest.raises()
        assert division_4(middle, end)

