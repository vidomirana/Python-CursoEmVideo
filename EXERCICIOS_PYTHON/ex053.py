#Verificar se a frase é um palíndromo, desconsiderando espaços e acentos
frase = str(input('Digite uma frase: '))
frase = frase.lower().replace(' ', '')
caracteres = list(frase)
inverso = caracteres[::-1]

if caracteres == inverso:
    print('Frase É PALÍNDROMO')
else:
    print('Frase NÃO é palíndromo')
