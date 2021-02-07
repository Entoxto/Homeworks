"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
from os import remove

with open("5.1.txt", "w", encoding='UTF-8') as file:
    stroki = []
    print(f"----------Чтобы ввести очередную строку, введите Enter\n----------Чтобы закончить ввод, оставьте строку пустой и нажмите Enter\n\n##### cпособ 1:\n")
    while True:
        a = input("Введите строку: ")
        if a == "":
            break
        else:
            stroki.append(a + "\n")
    file.writelines(stroki)

with open("5.1.txt", "r", encoding='UTF-8') as file:
    print(file.read())

remove("5.1.txt")

print("##### cпособ 2:\n")
with open("5.1.txt", "a", encoding='UTF-8') as file:
    while True:
        a = input("Введите строку: ")
        if a == "":
            break
        else:
            file.write(a + "\n")

with open("5.1.txt", "r", encoding='UTF-8') as file:
    print(file.read())
