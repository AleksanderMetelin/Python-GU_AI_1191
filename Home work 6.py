'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
'''

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


a = TrafficLight()
a.running()

'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''


class Road:
    _length = 0
    _width = 0

    def mass(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth
        total = self._length * self._width * self.weight * self.depth / 1000
        return print(f"Масса асфальта\n {self._length} м * {self._width} м * {self.weight} кг "f"* {self.depth} см = ",
                     total, "т")


r = Road()
r.mass(20, 5000, 25, 10)

'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


a = Position('Александр', 'Петров', 'главный механик', 20000, 5000)

print(a.name)
print(a.surname)
print(a.position)
print(f'Сотрудник {a.get_full_name()} в должности {a.position} получает полную зарплату '
      f'в размере {a.get_total_income()} рублей')

'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go_stop(self):
        if self.speed != 0:
            return f' Автомобиль начал движение и движется со скоростью {self.speed} км/ч. '
        else:
            return 'Автомобиль стоит на месте'

    def turn(self):
        a = ['налево', 'направо']
        return random.choice(a)

    def show_speed(self):
        return f'Текущая скорость автомобиля состовляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км\ч превышает разрешенную скорость'
        else:
            return f'{self.speed} км\ч не превышает разрешенную скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} превышает разрешенную скорость'
        else:
            return f'{self.speed} не превышает разрешенную скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


a = Car(0, 'red', 'Ford', False)
b = TownCar(100, 'баклажан', 'Lada Kalina', False)
c = WorkCar(39, 'белый', 'Kamaz', False)
d = PoliceCar(150, 'черный', 'toyota_corolla', True)

print(f'Автомобиль {c.name} цвет {c.color}, движется со скоростью {c.show_speed()} , он поворачивает {c.turn()}'
      f'\nЗа ним Автомобиль {b.name} цвет {b.color}, движется со скоростью {b.show_speed()} , он поворачивает {b.turn()}')

'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки в ученической тетради с помощью {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки в черно-белых тонах с помощью {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки в учебнике, выделяем текст с помощью {self.title}'


pen = Pen('ручки')
pencil = Pencil('карандаша')
handle = Handle('маркера')

print(pen.draw())
print(pencil.draw())
print(handle.draw())
