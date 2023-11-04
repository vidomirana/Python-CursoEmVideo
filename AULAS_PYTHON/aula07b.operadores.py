## ------- Operadores Aritméticos ------- ##

# Ordem de procedência:
    # 1º  ()  parênteses
    # 2º ** potências
    # 3º *, /, //, %  Multiplicação, divisão, divisão inteira e resto da divisão
    # 4º  + e - adição e subtração binárias
# -------------------------------------------------------
#Exponenciação ---> pow(4, 3) == 4**3

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
r = n1%n2
e = pow(n1, n2)
print(f'A soma é {s}, \n o produto é {m}, a divisão é {(d):.2f} ', end=' ,')  # .2f == quero apenas duas casas após o ponto
print(f'a divisão inteira é {di}, o resto da divisão é {r} e a potência é {e}') #end=' ' == não dê parágrafo
# \n quebra a linha e dá um parágrafo