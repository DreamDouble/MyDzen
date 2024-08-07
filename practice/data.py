"""ЦИКЛЫ"""
"""цикл WHILE"""
i = 4
while i < 15:  # так как цикл старый выполняется медленнее остальных
    i = i + 1
    print(i)

"""цикл FOR"""
for i in 'hello world':  # выполняется быстрее, проходит по любому итерируемому объекту, при работе выполняет тело цикла
    print(i * 2, end='')

"""оператор CONTINUE"""
for i in 'hello world 123':
    if i == '0':
        continue  # continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
    print(i * 2, end='')

"""оператор BREAK"""
for i in 'ga ga ga la la la pipleo':
    if i == 'o':
        break
    print(i * 2, end='')

"""ELSE"""
for i in 'bla bla bla':
    if i == 'a':
        break
    else:
        print('много букв')