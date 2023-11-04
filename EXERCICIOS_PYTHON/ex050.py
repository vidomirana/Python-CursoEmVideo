#Ler seis números inteiros e somar apenas os pares
lista =[]

for i in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        lista.append(n)
soma = sum(lista)
print(f'A soma dos números pares é {soma}')
