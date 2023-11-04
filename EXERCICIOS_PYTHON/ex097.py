#Criar uma função para escrever uma linha adaptável ao tamanho do texto
def escreva(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


escreva(str(input('Escreva algo: ')))
