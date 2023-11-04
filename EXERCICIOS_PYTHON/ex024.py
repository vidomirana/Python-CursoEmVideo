#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome 'Santo' ou não

cidade = str(input('Digite o nome da cidade: ')).strip().title()
dividido = cidade.split()
print('Santo' in dividido[0:5])
