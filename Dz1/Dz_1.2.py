"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

a = int(input('time in sec: '))
while a < 0:
    if a < 0:
        print('please enter a>=0')
        a = int(input('time in sec: '))
hour = a//3600
min = (a-hour*3600)//60
sec = (a-hour*3600-min*60)
print(f'{hour:02d}:{min:02d}:{sec:02d}')
