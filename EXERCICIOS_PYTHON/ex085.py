#Numa lista unica, adicionar duas listas dentro com valores pares e ímpares, pedir 7 números
#Mostrar os pares em ordem e os ímpares também em ordem
valores = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i} número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]}')
print(f'Os valores ímpares digitados foram {valores[1]}')
