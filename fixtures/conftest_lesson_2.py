import pytest

"""этот файл в котором хранятся различные функции которые можно запускать в рамках всего пакета тестов,
в эту фикстуру мы вынесем метод для очистки файла для потом дальнейшего его заполнения"""

cnt = 0  # Создаем переменную cnt для 2го примера

#  Пример 1
@pytest.fixture(autouse=True)  # autouse = True - параметр отвечающий за очистку файла
def clean_text_file_1():
    with open('../test_data/read_from_file_lesson_2.txt', 'w'):
        pass

#  Пример 2
@pytest.fixture(autouse=True)  # autouse = True - параметр отвечающий за очистку файла
def clean_text_file_2():
    global cnt  # Объявляем переменную cnt глобальной
    with open('../test_data/read_from_file_lesson_2.txt', 'w'):
        pass
    print(cnt)
    cnt += 1  # Считаем сколько раз происходит запуск функции clean_text_file_2
