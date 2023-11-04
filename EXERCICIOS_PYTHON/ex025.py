#Crie um programa que diga se uma pessoa tem 'Silva' no nome

nome = str(input('Escreva seu nome: ')).title().strip()
if nome.find(' Silva ') == -1:
    print('Seu nome não tem Silva')
else:
    print('Seu nome tem Silva')#---------------------------------------
