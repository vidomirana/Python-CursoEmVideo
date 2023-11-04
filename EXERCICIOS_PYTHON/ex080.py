#Ler 4 números, colocar os números na lista na ordem crescente sem usar o .sort() nem o sorted()
valores = []
for v in range(0,4):
    n = int(input('Digite um valor: '))
    if len(valores) == 3:
        if n >= valores[2]:
            valores.append(n)
            print('Valor adicionado no final da lista')
        elif n <= valores[0]:
            valores.insert(0,n)
            print('Valor adicionado no início da lista')
        elif valores[0] < n <= valores[1]:
            valores.insert(1,n)
            print('Valor adicionado na posição 1')
        else:
            valores.insert(2,n)
            print('Valor adicionado na posição 2')
    if len(valores) == 2:
        if n >= valores[1]:
            valores.append(n)
            print('Valor adicionado no final da lista')
        elif n <= valores[0]:
            valores.insert(0,n)
            print('Valor adicionado no início da lista')
        else:
            valores.insert(1,n)
            print('Valor adicionado no meio da lista')
    if len(valores) == 1:
        if n >= valores[0]:
            valores.append(n)
            print('Valor adicionado ao final da lista')
        else:
            valores.insert(0,n)
            print('Valor adicionado no início da lista')
    if len(valores) == 0:
        valores.append(n)
        print('Valor adicionado ao final da lista')
print(f'Lista ordenada: {valores}')