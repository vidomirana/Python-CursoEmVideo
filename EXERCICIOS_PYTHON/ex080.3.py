#Ler 5 números, colocar os números na lista na ordem crescente sem usar o .sort() nem o sorted()
import bisect
valores = []
for i in range(5):
    n = int(input('Digite um número: '))
    bisect.insort(valores,n)
    print(f'Número adicionado na posição {valores.index(n)} da lista...')
print(f'Lista em ordem crescente: {valores}')
