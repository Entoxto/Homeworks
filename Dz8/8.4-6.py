"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""
from sys import exit
from time import sleep


class Int(Exception):
    pass


class Sklad:

    @classmethod
    def file_info(cls, name_file, go=None, stop=None):
        try:
            with open(name_file, "r", encoding="utf-8-sig") as file:
                number_of_printers = 0
                number_of_scanners = 0
                number_of_copiers = 0
                lines = file.readlines()
                lines = lines[go:stop]
            for stroka in lines:
                if stroka.find("Колличество принтеров") != -1:
                    number_of_printers = int(stroka.split(' = ')[1])
                elif stroka.find("Колличество сканеров") != -1:
                    number_of_scanners = int(stroka.split(' = ')[1])
                elif stroka.find("Колличество копировальных машин") != -1:
                    number_of_copiers = int(stroka.split(' = ')[1])
            return [number_of_printers, number_of_scanners, number_of_copiers]
        except FileNotFoundError:
            print("Такого файла не существует, повторите потытку!")

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price}руб'

    @classmethod
    def priem(cls, add):
        cl = [Copier, Scanner, Printer]
        new_sklad_info = Sklad.file_info("sklad.txt")
        counter = 2
        for i in cl:
            if isinstance(add, i):
                try:
                    n = input(f'Введите колличество объектов {add}, принимаемых на склад: ')
                    if not n.isdigit():
                        raise Int
                    else:
                        new_sklad_info[counter] += int(n)
                        break
                except Int:
                    print('Колличество товаров должно быть целым положительным числом, повторите попытку...')
            counter -= 1
        with open("sklad.txt", "w", encoding="utf-8-sig") as file:
            file.writelines([f'Колличество принтеров = {new_sklad_info[0]}\n',
                             f'Колличество сканеров = {new_sklad_info[1]}\n'
                             f'Колличество копировальных машин = {new_sklad_info[2]}'])
        return new_sklad_info

    @classmethod
    def peredacha(cls, otdel, tovar):
        cl = [Copier, Scanner, Printer]
        counter = 2
        otdel_org = {'Отдел ремонта': [0, 1], 'Отдел продаж': [4, 5], 'Отдел доставки': [8, 9]}
        otdel_len = {'Отдел ремонта': [1, 4], 'Отдел продаж': [5, 8], 'Отдел доставки': [9, 12]}
        if otdel != 'Отдел ремонта' and otdel != 'Отдел продаж' and otdel != 'Отдел доставки':
            return print('Такого отдела не существует!')
        sklad_info = Sklad.file_info('sklad.txt')
        ychet_info = Sklad.file_info("ychet.txt", otdel_len[otdel][0], otdel_len[otdel][1])
        for i in cl:
            if isinstance(tovar, i):
                try:
                    n = input(f'Введите колличество передоваемых {tovar}: ')
                    if not n.isdigit():
                        raise Int
                    else:
                        if sklad_info[counter] < int(n):
                            return print('Такого колличества нет на складе!')
                        sklad_info[counter] -= int(n)
                        ychet_info[counter] += int(n)
                        break
                except Int:
                    print('Колличество товаров должно быть целым положительным числом, повторите попытку...')

            else:
                counter -= 1

        b = [f'Колличество принтеров = {ychet_info[0]}\n',
             f'Колличество сканеров = {ychet_info[1]}\n',
             f'Колличество копировальных машин = {ychet_info[2]}\n']

        with open("ychet.txt", "r", encoding="utf-8-sig") as file:
            new_ychet = file.readlines()
        new_ychet[otdel_len[otdel][0]:otdel_len[otdel][1]] = b

        with open("sklad.txt", "w", encoding="utf-8-sig") as file:
            file.writelines([f'Колличество принтеров = {sklad_info[0]}\n',
                             f'Колличество сканеров = {sklad_info[1]}\n'
                             f'Колличество копировальных машин = {sklad_info[2]}'])

        with open("ychet.txt", "w", encoding="utf-8-sig") as file:
            file.writelines(new_ychet)

        print(f'Изменения успешно внесены!\nСостояние отдела: {otdel}: ')
        print_lines = [f'Колличество принтеров = {ychet_info[0]}',
                       f'Колличество сканеров = {ychet_info[1]}',
                       f'Колличество копировальных машин = {ychet_info[2]}']
        for i in print_lines:
            print(i)
        return ychet_info


class Scanner(Sklad):
    def __init__(self, name, price, resolution):
        super().__init__(name, price)
        self.resolution = resolution

    @staticmethod
    def to_scan():
        print('Подождите, идёт сканироание...')
        sleep(3)
        print('Сканирование завершено!')


class Printer(Sklad):
    def __init__(self, name, price, typing, print_colors=False):
        super().__init__(name, price)
        self.type = typing
        self.print_colors = print_colors

    @staticmethod
    def to_print():
        print('Печать запущена...')
        sleep(2)
        print('Печать завершена успешно!')


class Copier(Printer, Scanner):
    def __init__(self, name, price, typing, print_colors, speed_copy):
        self.name = name
        self.price = price
        self.speed_copy = speed_copy
        self.type = typing
        self.print_colors = print_colors

    @staticmethod
    def to_copier(number_of_copies):
        print('Старт копирования..')
        for i in range(number_of_copies):
            print(f'Идёт создание {i}-й копии... ')
        print('Копирование успешно завершено!')


b = Scanner('Сканер Canon', '2300', ' 2400x2400 dpi')
Sklad.priem(b)
b.to_scan()

a = Printer("Принтер HP", '4200', 'Струйный')
Sklad.priem(a)
a.to_print()

c = Copier('Копировальный аппарат xerox', '10000', 'лазерный', False, '30')
Sklad.priem(c)
c.to_scan()
c.to_print()
c.to_copier(3)

Sklad.peredacha('Отдел ремонта', a)
Sklad.peredacha('Отдел продаж', b)
Sklad.peredacha('Отдел доставки', c)
