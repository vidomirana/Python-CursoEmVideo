#Ler dois valores e mostrar um menu na tela
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
x = 99
print(' [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR VALOR \n [4] INSERIR NOVOS NÚMEROS \n [0] SAIR DO PROGRAMA')
while x != 0:
    x = int(input('Opção: '))
    if x == 1:
        print(f'A soma é {n1 + n2}!')
    elif x == 2:
        print(f'O produto é {n1 * n2}!')
    elif x == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}!')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}!')
        else:
            print('Os valores são iguais!')
    elif x == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    else:
        x = 0
print('PROGRAMA FINALIZADO!')

