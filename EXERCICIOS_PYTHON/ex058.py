#Melhorar o desafio 028
#Computador pensa num número, jogador tenta adivinhar até acertar
#Computador fala quantas tentativas precisou até acertar
from random import randint
comp = randint(1,10)
tentativas = 0
jogador = int(input('Qual número de 1 a 10 eu pensei?  --> '))
while jogador != comp:
    jogador = int(input('Errou! Tente novamente: '))
    tentativas += 1
print('Acertou!!')
print(f'Você precisou de {tentativas + 1} tentativas!')