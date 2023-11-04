## ------- Operadores Aritméticos ------- ##

# Ordem de procedência:
    # 1º  ()  parênteses
    # 2º ** potências
    # 3º *, /, //, %  Multiplicação, divisão, divisão inteira e resto da divisão
    # 4º  + e - adição e subtração binárias
# -------------------------------------------------------
#Exponenciação ---> pow(4, 3) == 4**3

nome = input('Qual seu nome? ')
print(f'Olá, {(nome):>25}')   #nome com 25 espaços à esquerda
print(f'Olá, {(nome):<25}')   #nome com 25 espaços à direita
print(f'Olá, {(nome):^25}')   #nome centralizado em 25 espaços
print(f'Olá, {(nome):=^25}')  #nome centralizado entre caracteres de =
