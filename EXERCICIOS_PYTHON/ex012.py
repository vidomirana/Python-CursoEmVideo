## Desconto de loja

preco = float(input('Insira o preço do produto:  '))
porc = int(input('Qual a porcentagem de desconto? (sem o %, apenas número)  '))

x = (porc/100)*preco
preco2 = preco - x

print(f'O preço com {porc}% de desconto é R${preco2:.2f}')
