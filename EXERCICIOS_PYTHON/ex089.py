#Armazenar nomes e duas notas dos alunos, mostrar o boletim de todos e as notas de algum aluno pedido
boletim = []
while True:
    alunos = []
    alunos.append(str(input('Aluno: ')))
    for nota in range(1,3):
        alunos.append(float(input(f'Nota {nota}: ')))
    boletim.append(alunos[:])
    resp = str(input('CONTINUAR? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break

print('N°', end='  ')
print(f'{"Aluno":^15}', end='  ')
print(f'{"Média":^15}')
print('-=' * 16)
for i in range(0, len(boletim)):
    print(i, end='   ')
    print(f'{boletim[i][0]:^15}', end=' ')
    print(f'{(boletim[i][1]  +  boletim[i][2]) / 2:^15.2f}')
print('-=' * 16)

while True:
    nomenotas = int(input('Ver notas do aluno [N°] (999 interrompe): '))
    if nomenotas == 999:
        break
    print(f'{boletim[nomenotas][0]} teve notas {boletim[nomenotas][1:]}')
    print('-=' * 20)
print('FINALIZADO...')
