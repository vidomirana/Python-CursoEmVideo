#Perguntar quantos jogos o usuário quer fazer na megasena e gerar os números
from random import sample
from time import sleep
print('-=' * 30)
print(f"{'JOGOS MEGA-SENA':^55}")
print('-=' * 30)

numeros = []
for v in range(1,61):
    numeros.append(v)

n = int(input('Sortear quantos jogos?  '))
print('-=' * 30)
for i in range(n):
    palpite = sample(numeros, 6)
    palpite.sort()
    print(palpite)
    palpite.clear()
    sleep(1)
print('-=' * 30)
print(f'{"BOA SORTE!":^55}')
print('-=' * 30)
