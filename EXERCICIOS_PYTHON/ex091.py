#4 jogadores jogam um dado, mostrar o ranking
from random import randint
from time import sleep
dado = {}
jogadas = []
for i in range(1,5):
    dado[f'jogador{i}'] = randint(1,6)
    jogadas.append(dado.copy())
    dado.clear()
for i in jogadas:
    for k, v in i.items():
        print(f'{k} jogou {v}')
        sleep(1)
ranking = sorted(jogadas, key=lambda x: list(x.values())[0], reverse=True)
print('RANKING: ')
for p, c in enumerate(ranking):
    for k, v in c.items():
        print(f'{p+1}° lugar: {k} com {v} pontos')
