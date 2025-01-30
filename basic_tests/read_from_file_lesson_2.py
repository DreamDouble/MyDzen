def read_from_file(filepath):
    with open(filepath, 'r') as f_o:  # f_o = file object аббревиатура как в sql. 'r' - режим чтения

        return f_o.readlines()


print('Проверка доступности файла:', (read_from_file('../test_data/read_from_file_lesson_2.txt')))

#  print('Проверка доступности файла:', (read_from_file('read_from_file_lesson_2.txt'))) если файл находится в том же модуле
