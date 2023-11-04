# Aumento de salário

sal = float(input('Insira o salário do funcionário: '))
aum = float(input('Insira a porcentagem de aumento (sem o %) '))

x = (aum/100)*sal
sal2 = sal+x

print(f'O novo salário do funcionário é R${sal2:.2f}')