nome = str(input('Qual o seu nome? '))
if nome == 'Vitor':
    print('Olá, Vitor!')
else:
    print('Quem é você?')
print('-----------------------------------')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Média: {m:.1f}')
if m >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')
