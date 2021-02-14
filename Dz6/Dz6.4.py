"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина поехала")

    def stop(self):
        print(f"Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на{direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}")


a = Car("60", "зелёный", "Ока")
print(
    f"Машина {a.name}, цвет {a.color}, скорость - {a.speed}, использование в полиции: {a.is_police}")
a.go()
a.show_speed()
a.turn("право")
a.stop()

print("----------------------------------------------------------------------------------")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Вы превысили скорость! Текущая скорость автомобиля : {self.speed}! "
                  f"Максимальная разрешённая скорость: 60")
        else:
            print(f"Текущая скорость автомобиля : {self.speed}")


b = TownCar("70", "чёрный", "Kia")
print(
    f"TownCar {b.name}, цвет {b.color}, скорость - {b.speed}, использование в полиции: {b.is_police}")
b.go()
b.show_speed()
b.turn("лево")
b.stop()
print("----------------------------------------------------------------------------------")


class SportCar(Car):
    pass


c = SportCar("200", "чёрный", "Audi")
print(
    f"SportCar {c.name}, цвет {c.color}, скорость - {c.speed}, использование в полиции: {c.is_police}")
c.go()
c.show_speed()
c.turn("право")
c.stop()
print("----------------------------------------------------------------------------------")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Вы превысили скорость! Текущая скорость автомобиля : {self.speed}! "
                  f"Максимальная разрешённая скорость: 40")
        else:
            print(f"Текущая скорость автомобиля : {self.speed}")


d = WorkCar("45", "жёлтый", "Погрузчик")
print(
    f"WorkCar {d.name}, цвет {d.color}, скорость - {d.speed}, использование в полиции: {d.is_police}")
d.go()
d.show_speed()
d.turn("лево")
d.stop()
print("----------------------------------------------------------------------------------")


class PoliceCa(Car):
    pass


i = PoliceCa("150", "синий", "Ford", True)
print(
    f"PoliceCa {i.name}, цвет {i.color}, скорость - {i.speed}, использование в полиции: {i.is_police}")
i.go()
i.show_speed()
i.turn("право")
i.stop()
