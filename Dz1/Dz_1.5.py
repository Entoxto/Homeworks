# Запросите у пользователя значения выручки и издержек фирмы.
revenue = float(input('revenue: '))
costs = float(input('costs: '))
while revenue < 0 or costs < 0:
    if revenue < 0 or costs < 0:
        print('please enter values>=0')
        revenue = float(input('revenue: '))
        costs = float(input('costs: '))
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
if revenue > costs:
    print('revenue>costs')
    # Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
    profitability = revenue/costs
    print(f'profitability= {profitability}' )
    # Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника
    number_of_employees = int(input('number of employees: '))
    while number_of_employees <= 0:
        if number_of_employees <= 0:
            print('please enter values>0')
            number_of_employees = int(input('number of employees: '))
    profitability_in_one_employees=profitability/number_of_employees
    print(f'profitability_in_one_employees= {profitability_in_one_employees}')
else: print('revenue<costs')