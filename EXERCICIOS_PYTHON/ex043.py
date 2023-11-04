#Cálculo e classificação de Índice de Massa Corporal

peso = float(input('Insira apenas o valor do seu peso: '))
altura = float(input('Insira apenas o valor da sua altura em metros: '))
IMC = peso / (altura ** 2)

print(f'Seu IMC é {IMC:.1f}', end= ' ')
if IMC < 18.5:
    print('e você está abaixo do peso')
elif IMC < 25:
    print('e você está no peso ideal')
elif IMC < 30:
    print('e você está com sobrepeso')
elif IMC < 40:
    print('e você está com obesidade')
else:
    print('e você está com obesidade mórbida')