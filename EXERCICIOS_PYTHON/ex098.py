#Contagem com passo
from time import sleep


def cabecalho(txt):
    print('-=' * len(txt))
    print(txt)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    while True:
        sleep(0.2)
        print(inicio, end=' ')
        if inicio > fim:
            inicio -= abs(passo)
        elif inicio == fim:
            break
        else:
            inicio += abs(passo)
    print('FIM!')


cabecalho('CONTAGEM DE 1 a 10 de 1 em 1')
contador(1, 10, 1)
cabecalho('CONTAGEM DE 10 a 0 de 2 em 2')
contador(10, 0, 2)
print('AGORA VOCÊ ESCOLHE')

while True:
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p == 0:
        cabecalho(f'CONTAGEM DE {i} a {f} de 1 em 1')
    else:
        cabecalho(f'CONTAGEM DE {i} a {f} de {abs(p)} em {abs(p)}')
    contador(i, f, p)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('==== FINALIZADO ====')
