#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
a = int(input('number: '))
b = a+(a*10+a)+(a*100+a*10+a)
print(b)

