#Contagem regressiva para os fogos
from time import sleep
n = int(input('Insira a quantidade de segundos para os fogos: '))
for i in range(n, 0, -1):
    print(i)
    sleep(1)
print('-=-=-=-=FELIZ ANO NOVO!!=-=-=-=-')