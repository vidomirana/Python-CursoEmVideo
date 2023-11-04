#Pedir o sexo de uma pessoa até ela digitar F ou M

sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
        sexo = str(input('INVÁLIDO, TENTE NOVAMENTE: ')).strip().upper()[0]
print('Fim')

