#Tabuada de vários valores e parar programa com número negativo

while True:
    n = int(input('Quer ver a tabuada de qual valor? [número negativo p/ finalizar]: '))
    if n < 0:
        break
    c = 0
    print('-=' * 10)
    while c != 10:
        c += 1
        print(f'{n} x {c} = {n * c}')
    print('-=' * 10)
print('Programa finalizado!')