#Aproveitamento de um jogador
from operator import index
jogador = {'nome': str(input('Nome do jogador: '))}
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
jogador['gols'] = []
for i in range(1, jogador['partidas'] + 1):
    jogador['gols'].append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i}? :  ')))
jogador['total'] = sum(jogador['gols'])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for i in range(1, jogador['partidas'] + 1):
    print(f'   => Na partida {i}, fez {jogador["gols"][i-1]} gols')

