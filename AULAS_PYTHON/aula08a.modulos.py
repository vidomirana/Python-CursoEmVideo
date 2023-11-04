from math import sqrt, ceil
import random
import emoji

n = float(input('Digite um número: '))
raiz = sqrt(n)
print(f'A raíz quadrada do número é {ceil(raiz):.3f}') #ceil arredonda pra cima

print('============================================')

aleat = random.random()  #atribuir um número real entre 0 e 1 à variável
aleat2 = random.randint(1, 10) #atribui um número inteiro aleatório entre 1 e 10
print(aleat)
print(aleat2)
print(emoji.emojize('Olá, Mundo! :smiling_imp:', language='alias')) #usar um emoji

