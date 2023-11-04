#Simulador de caixa eletrônico, cédulas de 50, 20, 10 e 1
cedula_50 = cedula_20 = cedula_10 = cedula_01 = resto = 0

while True:     #notas de 50
    valor = int(input('Digite o valor a ser sacado: R$'))
    if valor % 50 == 0:
        cedula_50 = valor // 50
        break
    else:
        cedula_50 = valor // 50
        resto = (valor % 50)
        break
while True:   #notas de 20
    if resto % 20 == 0:
        cedula_20 = resto // 20
        break
    else:
        cedula_20 = resto // 20
        resto = resto % 20
        break
while True:     #notas de 10
    if resto % 10 == 0:
        cedula_10 = resto // 10
        break
    else:
        cedula_10 = resto // 10
        resto = resto % 10
        break
while True:    #notas de 1
    cedula_01 = resto // 1
    break

print('-~~' * 15)
print(f'{cedula_50} cédulas de R$50,00\n{cedula_20} cédulas de R$20,00\n{cedula_10} cédulas de R$10,00\n{cedula_01} cédulas de R$1,00')
print('-~~' * 15)