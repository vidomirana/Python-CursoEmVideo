#Mostrar parte inteira de um número real
from math import trunc
n = float(input('Digite um número real: '))
ntrunc = trunc(n)
print(f'A parte inteira desse número é {ntrunc}') #método trunc
print(f'A parte inteira desse número é {(n//1):.0f}') #método divisão inteira
