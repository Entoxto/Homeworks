"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    position = {"Геннадий Морозов": "сантехник", "Клавдия Кузовова": "уборщица", "Игнат Рабинович": "директор"}
    _income = {"сантехник": {"wage": 50000, "bonus": 10000},
               "уборщица": {"wage": 20000, "bonus": 5000},
               "директор": {"wage": 150000, "bonus": 50000}}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position(Worker):
    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        try:
            print(Worker._income[Worker.position[self.name + " " + self.surname]]["wage"] +
                  Worker._income[Worker.position[self.name + " " + self.surname]]["bonus"])
        except KeyError:
            print("Такого сотрудника у нас нет...")


a = Position("Геннадий", "Морозов")
a.get_full_name()
a.get_total_income()
