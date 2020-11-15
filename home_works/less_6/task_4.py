"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:

    def __init__(self, speed, colour, name, is_police=bool):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость состовляет {self.speed} km/h')


class TownCar(Car):
    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость состовляет {self.speed} km/h')
        else:
            print(f'Превыщение скорости на {self.speed - 60} km/h')


class SportCar(Car):
    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость состовляет {self.speed} km/h')
        else:
            print(f'Превыщение скорости на {self.speed - 40} km/h')


class PoliceCar(Car):
    def __init__(self, speed, colour, name, is_police=True):
        super().__init__(speed, colour, name, is_police)


town_car = TownCar(65,'black', 'Toyota')

town_car.go()
town_car.turn('лево')
town_car.show_speed()
town_car.stop()

print(town_car.is_police)

work_car = WorkCar(30, 'White', 'Cat')
work_car.show_speed()

print(work_car.colour)
