def read_from_file(filepath):
    with open(filepath, 'r') as f_o:  # f_o = file object

        return f_o.readlines()


#  print('Проверка доступности файла:', (read_from_file('../test_data/read_from_file.txt')))
