#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
# se não o empréstimo será negado.

valor = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira seu salário: R$'))
anos = int(input('Em quantos anos pretende pagar?: '))
parcela = valor / (anos * 12)

if parcela <= salario * 0.30:
    print('Empréstimo \033[32mAPROVADO\033[m')
else:
    print('Empréstimo \033[31mNEGADO\033[m')
    print('Valor da parcela excede 30% de seu salário')
print(f'Valor da parcela: R${parcela:.2f}')