"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

_, working_hours, rate_per_hour, bonus = argv


def zp(working_hours, rate_per_hour, bonus):
    working_hours = float(working_hours)
    rate_per_hour = float(rate_per_hour)
    bonus = float(bonus)
    c = working_hours * rate_per_hour + bonus
    return c


print(zp(working_hours, rate_per_hour, bonus))
