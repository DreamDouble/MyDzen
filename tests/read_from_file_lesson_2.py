from basic_tests.read_from_file_lesson_2 import read_from_file
from fixtures.conftest_lesson_2 import clean_text_file_1


def create_test_data(test_data):  # test_data приходит в качестве параметра. Этот тест test_read_from_file_3
    with open('../test_data/read_from_file_lesson_2.txt') as f_o:
        f_o.writelines(test_data)

def test_read_from_file():
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']  # Создаем переменную test_data в которую вкладываем значения
    assert test_data == read_from_file('../test_data/read_from_file_lesson_2.txt')  # Сравниваем значения test_data and read_from

def test_read_from_file_2():
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    assert test_data == read_from_file('../test_data/read_from_file_lesson_2.txt')

def test_read_from_file_3():
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    create_test_data(test_data)
    assert test_data == read_from_file('../test_data/read_from_file_lesson_2.txt')


"""Тесты на проверку с процессом наполнения"""


def test_read_from_file_4():  # Создаем функцию
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']  # Создаем переменную и вкладываем в нее данные на проверку. Эти данные он создает в файле
    with open('../test_data/read_from_file_lesson_2.txt', 'a') as file:  # Вызываем оператор with для работы с файлами. 'a' - это способ работы с файлом, можно изменить на 'w'
        file.writelines(test_data)  # записываем в файл с помощью метода writelines
    assert test_data == read_from_file('../test_data/read_from_file_lesson_2.txt')  # сравниваем через assert данные


"""Тесты на проверку с процессом очистки и дальнейшим наполнением"""


def test_read_from_file_5():
    with open('../test_data/read_from_file_lesson_2.txt', 'w'):  # с помощью "w" вычищаем файл
        pass
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    with open('../test_data/read_from_file_lesson_2.txt', 'a') as file:  # с помощью "a" заполняем файл
        file.writelines(test_data)
    assert test_data == read_from_file('../test_data/read_from_file_lesson_2.txt')


"""Тесты на проверку с процессом очистки с помощью фикстуры двумя способами"""


def test_read_from_file_6():
    clear = clean_text_file_1  # очищение файла теперь проходит с помощью фикстуры clean_text_file
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    with open('../test_data/read_from_file_lesson_2.txt', 'a') as file:
        file.writelines(test_data)
    assert test_data == read_from_file('../test_data/read_from_file_lesson_2.txt')

def test_read_from_file_7(clean_text_file_1):  # очищение файла теперь проходит с помощью фикстуры clean_text_file
    test_data = ['one - 1\n', 'two - 2\n', 'three - 3']
    with open('../test_data/read_from_file_lesson_2.txt', 'a') as file:
        file.writelines(test_data)
    assert test_data == read_from_file('../test_data/read_from_file_lesson_2.txt')