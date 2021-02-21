"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, 
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import datetime

class Data:
    _d_day = [1, 31]
    _d_month = [1, 12]
    _d_year = [0, datetime.datetime.today().year]

    def __init__(self, day, month, year):
        Data.int_method(day, month, year)
        self.day = Data.validation(Data._d_day[0], day, month, year, Data._d_day[1])
        self.month = Data.validation(Data._d_month[0], month, month, year, Data._d_month[1])
        self.year = Data.validation(Data._d_year[0], year, month, year, Data._d_year[1])

    def __str__(self):
        return f'{self.day, self.month, self.year}'

    @classmethod
    def int_method(cls, day, month, year):
        int(day)
        int(month)
        int(year)

    @staticmethod
    def validation(start, n, mounth, year, stop):
        if stop == 31:
            if mounth == 4 or 6 or 9 or 11:
                stop = 30
            if mounth == 2:
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    stop = 29
                else:
                    stop = 28

        if start <= n <= stop:
            return n
        else:
            return "Вне диапазона"


a = Data(29, 2, 2008)
print(a)
