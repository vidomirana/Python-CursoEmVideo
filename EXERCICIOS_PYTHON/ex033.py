# Como fiz
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
print('----------------------------------------')
# Método melhor com lista
lista = [n1, n2, n3]
lista_ordenada = sorted(lista)

print(f'O maior número foi: \033[32m{lista_ordenada[2]}\033[m')
print(f'O menor número foi: \033[31m{lista_ordenada[0]}')
