#Transformar um número inteiro em binário, octadecimal ou hexadecimal
num = int(input('Digite um número inteiro: '))
print('Digite 2 para conversão binária, 8 para octal ou 16 para hexadecimal')
conv = int(input('Opção: '))
if conv == 2:
    print(f'Binário: {bin(num)[2:]}')
elif conv == 8:
    print(f'Octadecimal: {oct(num)}')
elif conv == 16:
    print(f'Hexadecimal: {hex(num)}')
else:
    print('Reinicie o programa...')
