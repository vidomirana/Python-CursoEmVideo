# Selecionar ordem de apresentação
from random import shuffle, sample
print('Digite o nome dos alunos abaixo para ser feito o sorteio: ')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
a5 = str(input('Aluno 5: '))
lista = [a1, a2, a3, a4, a5]
shuffle(lista)     #Também posso usar sample((lista), k) sendo k a quantidade de itens a serem escolhidos da lista

print('Ordem de apresentação: ')
print(lista)
#-------------usando sample-------------------
escolhidos = sample(lista, 3)
print(escolhidos)