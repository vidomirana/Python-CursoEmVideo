#adicionar apenas valores inéditos na lista e mostrar em ordem crescente
lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado NÃO foi adicionado!')
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('=-=-' * 10)
print(f'Valores digitados: {sorted(lista)}')
