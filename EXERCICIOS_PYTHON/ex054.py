#Ler 7 datas de nascimento e mostrar quantas pessoas já atingiram a maioridade
from datetime import datetime
lista = []
maioridade = (365 * 18) + 4
contagem_maior = 0
contagem_menor = 0

for i in range(1,2):
    nascimento = input('Insira sua data de nascimento DD/MM/AAAA: ')
    nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
    dif = abs((datetime.today() - nascimento).days)
    lista.append(dif)

for dias in lista:
    if dias >= maioridade:
        contagem_maior += 1
    else:
        contagem_menor += 1

print(f'Existem {contagem_maior} pessoas com maioridade e {contagem_menor} pessoas com menoridade')