#Análise de números numa tupla
n1 = int(input(f'Digite 0 1° número inteiro: '))
n2 = int(input(f'Digite o 2° número inteiro: '))
n3 = int(input(f'Digite o 3° número inteiro: '))
n4 = int(input(f'Digite o 4° número inteiro: '))
numeros = (n1, n2, n3, n4)
print(numeros)
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro 3 está na {numeros.index(3) + 1}ª posição')
else:
    print('Não foi digitado o número 3')
print('Os valores pares foram: ')
for valor in numeros:
    if valor % 2 == 0:
        print(valor, end=' ')
