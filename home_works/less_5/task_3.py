"""
3. Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.

Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('task_3.txt', 'r', encoding='utf-8')as file:
    total = 0
    workers = 0
    chip_workers = []
    for line in file:
        lst = line.split()
        total += int(lst[1])
        workers += 1
        if int(lst[1]) < 20000:
            chip_workers.append(lst[0])

    print('Оклад менее 20000 у сотрудников:', ', '.join(chip_workers))
    print('Cредняя величина дохода сотрудников:', round(total/workers, 2))
