#Calcular a soma entre todos números ímpares, múltiplos de 3, entre 1 e 500
s = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
print(f'A soma é: {s}')
