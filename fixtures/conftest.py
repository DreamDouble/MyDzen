import pytest

# этот файл в котором хранятся различные функции которые можно запускать в рамках всего пакета тестов.

# в эту фикстуру мы вынесем метод для очистки файла для потом дальнейшего его заполнения

@pytest.fixture(autouse=True)  # autouse - параметр
def clean_text_file():
    with open('../test_data/read_from_file.txt', 'w'):
        pass
