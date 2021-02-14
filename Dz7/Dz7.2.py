"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    consumption_coat = 0
    consumption_costume = 0

    def __init__(self, r=None):
        self.r = r

    @abstractmethod
    def consumption(self):
        return f'Всего потребуется {Clothes.consumption_coat + Clothes.consumption_costume:.2f} метров ткани'

    @property
    def consumption(self):
        return f'Всего потребуется {Clothes.consumption_coat + Clothes.consumption_costume:.2f} метров ткани'


class Coat(Clothes):
    def consumption(self):
        Clothes.consumption_coat = self.r / 6.5 + 0.5
        return f'Для пошива пальто требуется {Clothes.consumption_coat:.2f} метров ткани'


class Costume(Clothes):
    def consumption(self):
        Clothes.consumption_costume = 2 * self.r + 0.3
        return f'Для пошива пальто требуется {Clothes.consumption_costume:.2f} метров ткани'


a = Coat(10)
print(a.consumption())

b = Costume(2)
print(b.consumption())

c = Clothes(1)
print(c.consumption)
