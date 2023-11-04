# Cálculo de hipotenusa
from math import sqrt, hypot

cato = float(input('Informe o valor do cateto oposto: '))
cata = float(input('Informe o valor do cateto adjacente'))
hip = sqrt((pow(cato, 2)) + (pow(cata, 2)))
hyp = hypot(cato, cata)

print(f'O valor da hipotenusa desse triângulo é {(hip):.3f}')
print(f'A hipotenusa vale {(hyp):.3f}') #usando a função hypot do módulo math
