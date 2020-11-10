"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).

Пример списка: [
    {“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
    {“average_profit”: 2000}
    ].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('task_7.txt', 'r', encoding='utf-8') as file:
    profit_dict = {}
    for line in file:
        lst = line.split()
        name = lst[0]
        revenue = lst[2]
        costs = lst[3]
        try:
            profit = int(revenue) - int(costs)
            profit_dict[name] = profit
        except ValueError:
            print(f'Ошибка в данных {revenue} или/и {costs}. В строке {name}')


    total = 0
    count = 0
    for val in profit_dict.values():
        if val > 0:
            total += val
            count += 1

    average_prof_dict = {"average_profit": total / count }

    data_list = [profit_dict, average_prof_dict]

    with open('task_7.json', 'w') as json_file:
        json.dump(data_list, json_file)