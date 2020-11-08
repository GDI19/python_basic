"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее
на экран.
"""
from functools import reduce

with open('task_5.txt', 'w', encoding='utf-8') as file:
    numbers = [32, 63, 76, 54, 89, 34, 63, 86, 56, 78]
    for d in numbers:
        file.write(str(d) + ' ')

with open('task_5.txt', 'r', encoding='utf-8') as file:
    content = ''.join(file.readlines())
    try:
        digits = [int(d) for d in content.split()]
        print(reduce(lambda x, y: int(x) + int(y), digits))
    except ValueError as e:
        print('Ошибка в данных', e)