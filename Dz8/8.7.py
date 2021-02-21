"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    I = 'i'
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'({self.a} + {self.b}{ComplexNumber.I}) + ({other.a} + {other.b}{ComplexNumber.I}) = ' \
               f'{self.a + other.a} + {self.b + other.b} {ComplexNumber.I}'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'({self.a} + {self.b}{ComplexNumber.I})*({other.a} + {other.b}{ComplexNumber.I}) = ' \
               f'{self.a * other.a - (self.b * other.b)} + {self.a * other.b + self.b*other.a}{ComplexNumber.I}'

    def __str__(self):
        return f'{self.a} + {self.b}{ComplexNumber.I}'


a = ComplexNumber(5, -3)
b = ComplexNumber(2, 7)

print(a + b)
print(a * b)
