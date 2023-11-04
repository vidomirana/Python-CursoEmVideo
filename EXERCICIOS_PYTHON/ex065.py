#Ler vários números, parar com 999, informar o maior valor e o menor, e informar a média
lista = []
i = s = n = 0
while n != 999:
    i += 1
    n = float(input(f'Digite o {i}° número: '))
    s += n
    lista.append(n)
s = s - 999
lista.pop(-1)
media = s / len(lista)
print(f'O maior número digitado foi {max(lista)}, o menor foi {min(lista)}, a soma {s} e a média {media}')

