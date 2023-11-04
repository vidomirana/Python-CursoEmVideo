#Ler vários números, mostrar quantos valores foram digitados, mostrar na ordem decrescente
#e falar se o 5 faz parte da lista
valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram digitados {len(valores)} elementos')
valores.sort(reverse=True)
print(f'A ordem decrescente é {valores}')
if 5 in valores:
    print(f'O valor 5 está nas posições: ', end='')
    for p, v in enumerate(valores):
        if v == 5:
            print(p, end=' ')
else:
    print('O valor 5 não se encontra na lista')
