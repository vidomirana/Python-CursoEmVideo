num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('Este número é \033[7;30;107mpar!\033[m')
else:
    print('Este número é \033[7;107;40mímpar!\033[m')
