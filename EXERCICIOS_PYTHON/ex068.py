#Jogando par ou ímpar
from random import randint
print('-=' * 8, 'Vamos jogar PAR OU ÍMPAR!', '-=' * 8)
c = 0
while True:
    choice_player = int(input('Digite [1] para ímpar e [2] para par: '))
    if choice_player == 1:
        choice_comp = 2
    else:
        choice_comp = 1
    comp = randint(1,2)
    player = int(input('Agora jogue seu número: '))
    if player % 2 == 0:
        player = 2
    else:
        player = 1
    if choice_comp == 1:
        if comp != player:
            print(f'Você perdeu, joguei {comp} e deu ÍMPAR!')
            break
        else:
            print(f'Parabéns! Joguei {comp} e deu PAR!')
            c += 1
    if choice_comp == 2:
        if comp != player:
            print(f'Parabéns! Joguei {comp} e deu ÍMPAR!')
            c += 1
        else:
            print(f'Você perdeu, joguei {comp} e deu PAR!')
            break
    print('-=' * 15)
    print(f'Rodada {c} finalizada!')
    print('-=' * 15)
print(f'Você venceu {c}x consecutivas!')