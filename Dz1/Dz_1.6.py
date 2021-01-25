a = int(input('a=: '))
b = int(input('b=: '))
while a <= 0 or b <= 0:
    if a <= 0 or b <= 0:
        print('please enter values>0')
        a = int(input('a=: '))
        b = int(input('b=: '))
day=1
print(f'{day}-й день: {a:.2f}')
while b >= a:
    a *= 1.1
    day += 1
    print(f'{day}-й день: {a:.2f}')
print(f'на {day}-й день спортсмен достиг результата — не менее {b} км.')
