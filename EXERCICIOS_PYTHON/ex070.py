#Cadastrar o nome e preço dos produtos, ao final mostrar o valor da compra
#Quantos produtos custaram mais que R$ 1000,00 e qual foi o produto mais barato
print('===' * 12, '\n')
print('~~' * 5, 'LOJAS MIRANDA', '~~' * 5, '\n')
print('===' * 12)
conta = c = mais_de_mil = 0
barato = ''
menor_valor = 99999999999
while True:
    produto = str(input('PRODUTO: ')).strip().upper()
    while True:
        preco = float(input('PREÇO: R$ '))
        if preco >= 0:
            break
    if preco > 1000:
        mais_de_mil += 1
    c += 1
    conta += preco
    if preco < menor_valor:
        menor_valor = preco
        barato = produto
    print('-=' * 20)
    decisao = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    print('-=' * 20)
    while True:
        if decisao in 'SsNn':
            break
        else:
            decisao = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    if decisao == 'N':
        break
print(f'{c} PRODUTOS TOTALIZANDO: R$ {conta:.2f} \n{mais_de_mil} produtos custaram mais de R$1000,00')
print(f'Produto mais barato: {barato} que custa R$ {menor_valor:.2f}')