#Gerar 5 números aleatórios, armazenar numa TUPLA e mostrar o maior e menor número
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nMaior número: {max(numeros)} \nMenor número: {min(numeros)}')