#4 empresas irão pedir produtos, determinar quantas empresas encomendaram o produto A
#Qual o nome da empresa que encaminhou a maior quantidade de algum produto
empresa_maiorqtd = ''
cont_emp_A = 0
maior_qtd = 0

for emp in range(1,5):
    empresa = str(input(f'Nome da {emp}ª empresa: ')).strip().upper()
    produto = str(input('Produto [A, B ou C]: ')).strip().upper()
    quantidade = int(input('Quantidade: '))
    if emp == 1:
        maior_qtd = quantidade
        empresa_maiorqtd = empresa
    if produto == 'A':
        cont_emp_A += 1
    if quantidade > maior_qtd:
        maior_qtd = quantidade
        empresa_maiorqtd = empresa

print(f'{cont_emp_A} empresas pediram o produto A')
print(f'{empresa_maiorqtd} foi a empresa que pediu maior quantidade de qualquer produto')
