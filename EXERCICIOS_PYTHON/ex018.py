# Informar seno, cosseno e tangente de um ângulo
from math import pi, sin, tan, cos
ang = float(input('Informe o grau do ângulo: '))
rad = ang * pi / 180
sen = sin(rad)
cos = cos(rad)
tg = tan(rad)

print('Informações desse ângulo: ')
print(f' Seno = {(sen):.3f} \n Cosseno = {(cos):.3f} \n Tangente = {(tg):.3f}')
