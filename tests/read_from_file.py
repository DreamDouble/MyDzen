from basic_tests.read_from_file import read_from_file
from fixtures.conftest import clean_text_file


def test_read_from_file():
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']  # Создаем переменную test_data в которую вкладываем значения
    assert test_data == read_from_file('../test_data/read_from_file.txt')  # Сравниваем значения test_data and read_from


def test_read_from_file_2():
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    assert test_data == read_from_file('../test_data/read_from_file.txt')


"""Тесты на проверку с процессом наполнения"""


def test_read_from_file_3():  # Создаем функцию
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']  # Создаем переменную и вкладываем в нее данные на проверку
    with open('../test_data/read_from_file.txt', 'a') as file:  # Вызываем оператор with для работы с файлами
        file.writelines(test_data)  # записываем в файл с помощью метода writelines
    assert test_data == read_from_file('../test_data/read_from_file.txt')  # сравниваем через assert данные


"""Тесты на проверку с процессом очистки и дальнейшим наполнением"""


def test_read_from_file_4():
    with open('../test_data/read_from_file.txt', 'w'):  # с помощью "w" вычищаем файл
        pass
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    with open('../test_data/read_from_file.txt', 'a') as file:  # с помощью "a" заполняем файл
        file.writelines(test_data)
    assert test_data == read_from_file('../test_data/read_from_file.txt')


"""Тесты на проверку с процессом очистки с помощью фикстуры двумя способами"""


def test_read_from_file_5():
    clear = clean_text_file  # очищение файла теперь проходит с помощью фикстуры clean_text_file
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    with open('../test_data/read_from_file.txt', 'a') as file:
        file.writelines(test_data)
    assert test_data == read_from_file('../test_data/read_from_file.txt')

def test_read_from_file_6(clean_text_file):  # очищение файла теперь проходит с помощью фикстуры clean_text_file
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    with open('../test_data/read_from_file.txt', 'a') as file:
        file.writelines(test_data)
    assert test_data == read_from_file('../test_data/read_from_file.txt')