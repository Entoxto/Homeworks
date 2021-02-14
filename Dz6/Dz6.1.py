"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep
from itertools import cycle


class TrafficLight:
    __color = 'red'

    def running(self, color=__color, stop=None):
        if color != TrafficLight.__color:
            TrafficLight.__color = color
        variants = {'red': [['red', 7], ['yellow', 2], ['green', 5]],
                    'yellow': [['yellow', 2], ['green', 5], ['red', 7]],
                    'green': [['green', 5], ['red', 7], ['yellow', 2]]}
        counter = 0
        for el in cycle(variants[TrafficLight.__color]):
            print(el[0])
            sleep(el[1])
            counter += 1
            if counter == stop:
                break


tl = TrafficLight()
tl.running('yellow', 6)
