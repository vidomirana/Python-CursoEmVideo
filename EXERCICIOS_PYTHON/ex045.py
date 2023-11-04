#Pedra, papel ou tesoura
from random import randint
from time import sleep
print('''Escolha sua opção:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input('Opção: '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO')
sleep(0.7)
computador = randint(1, 3)
if computador == 1:
    compchoice = 'PEDRA'
elif computador == 2:
    compchoice = 'PAPEL'
else:
    compchoice = 'TESOURA'

if jogador != 1 and jogador != 2 and jogador != 3:
    print('Opção INVÁLIDA, tente novamente')
else:
    if jogador == computador:
        print(f'O computador escolheu {compchoice}, portanto EMPATE')
    elif jogador - computador == -1:
        print(f'O computador escolheu {compchoice} portanto você PERDEU')
    elif jogador - computador == 1:
        print(f'O computador escolheu {compchoice}, portanto PARABÉNS! Você VENCEU')
    elif jogador - computador == -2:
        print(f'O computador escolheu {compchoice}, portanto PARABÉNS! Você VENCEU')
    elif jogador - computador == 2:
        print(f'O computador escolheu {compchoice} portanto você PERDEU')