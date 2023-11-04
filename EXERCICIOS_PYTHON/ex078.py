#adicionar valores na lista, mostrar o maior e menor número com suas respectivas posições
valores  = []
for i in range(0,5):
    valores.append(int(input(f'Digite o valor da posição {i}: ')))
print(f'O maior valor da lista foi {max(valores)} que está nas posições ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
         print(f'{c}...', end='')
print(f'\nO menor valor da lista foi {min(valores)} que está nas posições ', end='')
for p, val in enumerate(valores):
    if val == min(valores):
        print(f'{p}...', end='')
