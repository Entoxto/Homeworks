"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
with open("5.7.txt", encoding='UTF-8') as file:
    n = 0
    summa = 0
    sp = []
    profit_list = {}
    for line in file:
        line = line.split()
        m = list(map(int, line[2:]))
        profit = m[0] - m[1]
        print(f'Компания {line[0]} - прибыль:{profit} ')
        profit_list.update({line[0]: profit})
        if profit > 0:
            n += 1
            summa += profit

profit_middle = {'average_profit': summa / n}
print(f'Средняя прибыль компаний = {summa / n}')
sp.extend([profit_list, profit_middle])


with open('5.7.json', 'w', encoding='UTF-8') as file1:
    json.dump(sp, file1)

with open('5.7.json', 'r', encoding='UTF-8') as read_file:
    data = json.load(read_file)
    print(f'Data: {data}')
