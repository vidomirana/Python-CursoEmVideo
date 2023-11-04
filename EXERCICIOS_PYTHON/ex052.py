#Ler um número e dizer se ele é primo ou não
n = int(input('Digite um número inteiro: '))
lista = []
cont_zeros = 0

if n == 1 or n == 2:
    print('Esse número é PRIMO!')
elif n % 2 != 0:
    for i in range(1, n + 1):
        lista.append(n % i)
    for item in lista:
       if item == 0:
           cont_zeros += 1
    if cont_zeros == 2:
        print('Esse número é PRIMO!')
    else:
        print('Esse número não é primo!')
else:
    print('Esse número não é primo!')
