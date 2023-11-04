#Aprimorar o desafio 086 mostrando A) a soma de todos valores pares digitados
#B) a soma dos valores da terceira coluna
#C) o maior valor da segunda linha
matriz = [   [  ],  [  ],  [  ]   ]
for i in range(3):
    matriz[0].append(int(input(f'Digite o número da posição 0,{i}: ')))
for i in range(3):
    matriz[1].append(int(input(f'Digite o número da posição 1,{i}: ')))
for i in range(3):
    matriz[2].append(int(input(f'Digite o número da posição 2,{i}: ')))

print(f'[  {matriz[0][0]}  ][  {matriz[0][1]}  ][  {matriz[0][2]}  ]')
print(f'[  {matriz[1][0]}  ][  {matriz[1][1]}  ][  {matriz[1][2]}  ]')
print(f'[  {matriz[2][0]}  ][  {matriz[2][1]}  ][  {matriz[2][2]}  ]')

spares = 0
for v in matriz[0]:
    if v % 2 == 0:
        spares += v
for v in matriz[1]:
    if v % 2 == 0:
        spares += v
for v in matriz[2]:
    if v % 2 == 0:
        spares += v
print(f'A soma de todos números pares é {spares}')
print(f'A soma da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
