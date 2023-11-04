#Melhorar o desafio 093 cadastrando mais jogadores
time = []
while True:
    jogador = {'nome': str(input('Nome do jogador: '))}
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
    jogador['gols'] = []
    for i in range(1, jogador['partidas'] + 1):
        jogador['gols'].append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i}? :  ')))
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    resp = str(input('Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(time)
print('-=' * 30)
print('cod', end='  ')
print(f'{"Jogador":^15}', end='  ')
print(f'{"Gols":<15}', end='  ')
print(f'{"Total":>10}')
print('-=' * 30)
for i in range(1, len(time) + 1):
    print(f'{i}', end='  ')
    print(f'{time[i-1]["nome"]:^15}', end='  ')
    print(f'{str(time[i - 1]["gols"]):<15}', end='  ')
    print(f'{time[i-1]["total"]:>10}')
while True:
    while True:
        cod_jogador = int(input('Mostrar dados do jogador cod n° [999 interrompe]: '))
        if cod_jogador == 999 or cod_jogador > len(time):
            break
        print(f'=== LEVANTAMENTO DO JOGADOR {time[cod_jogador - 1]["nome"]}')
        for i in range(1, time[cod_jogador - 1]['partidas'] + 1):
            print(f'   No jogo {i} fez {time[cod_jogador - 1]["gols"][i - 1]} gols')
    if cod_jogador == 999:
        break
    print('Código inválido! Tente novamente...')
print(' ======== FINALIZADO =========')
