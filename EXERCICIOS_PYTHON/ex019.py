#Selecionar um aluno
from random import randint, choice
# ----------Alternativa 1 ---------------------
num = randint(1, 4)

if num == 1:
    print('Alberto')
if num == 2:
    print('Bruna')
if num == 3:
    print('Carlos')
if num == 4:
    print('Debora')

print('=======================')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolha = choice(lista)

print(f'O escolhido foi {escolha}')
