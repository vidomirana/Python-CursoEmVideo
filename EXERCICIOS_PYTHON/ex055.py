#Receber 5 pesos e informar qual o maior valor e o menor

lista = []

for i in range(1,6):
    peso = float(input('Insira o peso (kg): '))
    lista.append(peso)

maior_peso = max(lista)
menor_peso = min(lista)
print(f'O maior peso é {maior_peso}kg e o menor é {menor_peso}kg')