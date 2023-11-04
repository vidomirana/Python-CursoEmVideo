#Faça um programa que leia o nome completo de alguem e mostre apenas o primeiro e o último nome
nome = str(input('Digite seu nome completo: ')).strip().title()
dividido = nome.split()
invertido = dividido[::-1]
print(f'\033[35mPrimeiro nome: {dividido[0]} \nÚltimo nome: {invertido[0]}')
