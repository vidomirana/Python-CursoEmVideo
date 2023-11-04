#Ler vários valores e separar os pares e os ímpares em outras duas listas
valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    resp = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
pares = []
impares = []
valores.sort()
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Você digitou os valores {valores}')
print(f'Os números pares foram {pares}')
print(f'Os números ímpares foram {impares}')