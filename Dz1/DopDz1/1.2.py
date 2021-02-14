# Найти количество четных и нечетных чисел в списке
s = input("введите числа через пробел: ")
b = [int(i) for i in s.split() if i.isdigit()]
even_number = 0
un_even_number = 0
for x in b:
    if x % 2 != 0:
        un_even_number += 1
    else:
        even_number += 1
print(f'Колличество чётных чисел = {even_number}')
print(f'Колличество нечётных чисел = {un_even_number}')