"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open('task_1.txt', 'a', encoding='utf-8') as file:
    while True:
        string = input('Введите очередную строку для записи\nДля выхода нажмите enter при пустой строке: ')
        if string == '':
            break
        else:
            #file.write(string + '\n')
            print(string, file=file)
