#Ler nove números e mostrar uma matriz 3x3
matriz = [   [[], [], []],       [[], [], []],       [[], [], []]   ]
for i in range(3):
    matriz[0][i].append(int(input(f'Digite o número da posição 0,{i}: ')))
for i in range(3):
    matriz[1][i].append(int(input(f'Digite o número da posição 1,{i}: ')))
for i in range(3):
    matriz[2][i].append(int(input(f'Digite o número da posição 2,{i}: ')))

print(matriz[0][0], matriz[0][1], matriz[0][2])
print(matriz[1][0], matriz[1][1], matriz[1][2])
print(matriz[2][0], matriz[2][1], matriz[2][2])
