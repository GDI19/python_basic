"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

file_rus = open('task_4_rus.txt', 'a', encoding='utf-8')

with open('task_4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lst = line.split()
        if int(lst[2]) == 1:
            num = 'Один '
        elif int(lst[2]) == 2:
            num = 'Два '
        elif int(lst[2]) == 3:
            num = 'Три '
        elif int(lst[2]) == 4:
            num = 'Четыре '
        print(num + ' '.join(lst[1:]), file=file_rus )