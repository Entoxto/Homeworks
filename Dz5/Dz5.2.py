"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("5.1.txt", "r", encoding='UTF-8') as file:
    strok = 0
    words = 0
    for line in file:
        strok += 1
        words = len(line.split())
        print(f'строка {strok}: слов: {words}')
    print(f'Итого строк: {strok}')
