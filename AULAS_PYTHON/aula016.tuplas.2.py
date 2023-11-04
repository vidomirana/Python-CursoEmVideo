a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #A tupla c terá 7 elementos pois irá adicionar os elementos da b na a
print(c)
print('===========')
c = b + a
print(c)
print(c.count(5)) #Quantas vezes o número 5 aparece na tupla c
print(c.index(8)) #Em que posição está o 8?  PRIMEIRA OCORRÊNCIA
print(c.index(5, 1)) #ignora o primeiro 5
pessoa = ('Vitor', 23, 'M', 66.5)  #Tuplas aceitam vários tipos
del(pessoa)  #Apaga a tupla