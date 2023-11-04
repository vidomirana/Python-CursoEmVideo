#Classificação de categoria NATAÇÃO
from datetime import date

nascimento = int(input('Ano de nascimento do nadador: '))
hoje = date.today().year
idade = hoje - nascimento

if idade <= 9:
    print('CATEGORIA: MIRIM')
elif 9 < idade <= 14:
    print('CATEGORIA: INFANTIL')
elif 14 < idade <= 19:
    print('CATEGORIA: JUNIOR')
elif 19 < idade <= 25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')
