"""
    5. Запросите у пользователя значения выручки и издержек фирмы.
    Определите, с каким финансовым результатом работает фирма
    (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
    Выведите соответствующее сообщение. Если фирма отработала с прибылью,
     вычислите рентабельность выручки (соотношение прибыли к выручке).
     Далее запросите численность сотрудников фирмы и определите прибыль фирмы
     в расчете на одного сотрудника.
"""
revenues = int(input('Введите выручку компании: '))
costs = int(input('Введите издержки компании: '))
result = revenues - costs

if result > 0:
    print(f'За этот период компания получила прибыль: {result}')
    print('Рентабельность составила:', round((result/costs), 2))
    print()
    stuff = int(input('Введите количество сотрудников в вашей фирме: '))
    profit_per_person = round(result/stuff, 2)
    print('Прибыль фирмы в расчете на одного сотрудника составила:', profit_per_person)
else:
    print(f'За данный период компания понесла убытки: {result}')


