#Calcular preço a partir da forma de pagamento

preconormal = float(input('Digite o preço do produto: '))
print('Formas de pagamento:\n (1) A vista DINHEIRO/DÉBITO \n (2) 1x no CRÉDITO \n (3) 2x no CRÉDITO \n (4) 3x no CRÉDITO')
opcao = int(input('Escolha a opção: '))
opcao1 = preconormal * 0.9 #10% de desconto
opcao2 = preconormal * 0.95 #5% de desconto
opcao3 = preconormal
opcao4 = preconormal * 1.2 #20% de juros

if opcao == 1:
    print(f'O preço atualizado é R$ {opcao1:.2f}')
elif opcao == 2:
    print(f'O preço atualizado é R$ {opcao2:.2f}')
elif opcao == 3:
    print(f'O preço atualizado é R$ {opcao3:.2f}, com 2 parcelas de R$ {(opcao3 / 2):.2f}')
elif opcao == 4:
    print(f'O preço atualizado é R$ {opcao4:.2f}, com 3 parcelas de R$ {(opcao4 / 3):.2f}')
else:
    print('Opção INVÁLIDA')