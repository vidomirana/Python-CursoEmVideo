#Informar se o rapaz terá passou do tempo de alistamento, se falta ou se está na hora
#Informar também quanto tempo falta ou quanto tempo passou do prazo
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
dif = abs(idade - 18)

if idade < 18:
    print(f'Faltam {dif} anos para seu alistamento!')
elif idade > 18:
    print(f'Já se passaram {dif} anos desde seu alistamento obrigatório!')
else:
    print('Você precisa se alistar esse ano!')
