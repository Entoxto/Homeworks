"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

with open("5.5.txt", "w", encoding='UTF-8') as file:
    a = [randint(0, 300) for i in range(20)]
    a = ' '.join(map(str, a))
    file.write(a)

with open("5.5.txt", "r", encoding='UTF-8') as file:
    a = file.read().split()
    print(sum(map(int, a)))
