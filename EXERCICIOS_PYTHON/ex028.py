from random import randint
from time import sleep
nrandom = randint(1,5)
print('Pensei em um número entre 1 e 5... Consegue adivinhar?')
nusuario = int(input('Em que número pensei?  '))
print('Processando...')
sleep(2)  #Espera por 2 segundo
if nrandom == nusuario:
    print('\033[32mAcertou, miserável!!')
else:
    print(f'\033[31mErrou feio, errou rude!! Pensei no número {nrandom}')
