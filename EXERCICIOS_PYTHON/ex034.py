salario = float(input('Digite o salário do funcionário: '))
aumento1 = salario + (salario * 15/100)
aumento2 = salario + (salario * 10/100)

if salario > 1250:
    print(f'Funcionário receberá aumento de 10% e passará a receber \033[32mR${aumento2:.2f}')
else:
    print(f'Funcionário receberá aumento de 15% e passará a receber \033[32mR${aumento1:.2f}')
