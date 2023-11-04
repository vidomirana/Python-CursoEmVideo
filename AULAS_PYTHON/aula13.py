##Laços, repetições, iterações, for, in, range

for c in range(0,4):
    print('Teste')
print('Fim')
print('-=' * 15)

for i in range(1,3): #conta de 1 até 2
    print(i)
print('-=' * 15)

for a in range(4,0,-1): #conta de 4 até 1
    print(a)
print('-=' * 15)

for b in range(2, 11, 2): #Conta os pares de 2 à 10
    print(b)
print('-=' * 15)

num = int(input('Digite um número: '))
for x in range(1, num+1):    #conta até o numero que o usuario digitou
    print(x)
print('-=' * 15)

inicio = int(input('Digite o número do início da contagem: '))
fim = int(input('Digite o número de fim da contagem: '))
passo = int(input('Digite o passo da contagem: '))
for k in range(inicio, fim +1, passo):
    print(k)
print('-=' * 15)

s = 0
for l in range(1,4):
    op = int(input('Digite um número: '))
    s += op   #s vai recebendo a soma dos op digitados
print(f'A soma desses números deu {s}')