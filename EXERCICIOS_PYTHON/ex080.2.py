#Ler 5 números, colocar os números na lista na ordem crescente sem usar o .sort() nem o sorted()
valores = []
for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos,n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Lista em ordem crescente: {valores}')