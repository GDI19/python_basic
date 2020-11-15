"""
3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    _income = {
        'manager':{"wage": 45000, "bonus": 10000},
        'saller': {"wage": 25000, "bonus": 5000}
    }

    def __init__(self, name, surname, position, _income=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
    
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        income = self.get_total_income()
        print(full_name, income)

    def get_total_income(self):
        return Worker._income[self.position]['wage'] + Worker._income[self.position]['bonus']


one = Position('di', 'gar', 'manager')
one.get_full_name()

two = Position('M', 'Mos', 'saller')
two.get_full_name()