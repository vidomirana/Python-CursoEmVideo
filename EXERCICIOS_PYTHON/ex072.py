#Escrever um número por extenso usando tuplas
numeros = ('um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('Digite um número de 1 a 10: '))
    while n <= 0 or n > 10:
        n = int(input('Tente novamente. Digite um número de 1 a 10: '))
    extenso = numeros[n - 1]
    print(f'Você digitou o número {extenso}. ', end='')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('Programa finalizado!')
