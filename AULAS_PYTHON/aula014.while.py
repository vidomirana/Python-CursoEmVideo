'''for c in range(1,10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''n = 1
r = 'S'
while r == 'S':
    n = float(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''

x = 1
cont_pares = 0
cont_impares = 0
while x != 0:
    x = int(input('Digite um número: '))
    if x != 0:
        if x % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1

print(f'Foram digitados {cont_pares} números pares e {cont_impares} números ímpares.')
