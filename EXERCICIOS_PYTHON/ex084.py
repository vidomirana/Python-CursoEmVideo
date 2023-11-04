#Cadastrar nome e peso de várias pessoas, mostrar quantas pessoas foram cadastradas
#e quais são as pessoas mais pesadas e mais leves
pessoas = []
dados = []
c = maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [kg]: ')))
    pessoas.append(dados[:])
    if c == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    c += 1
    dados.clear()
    r = str(input('Continuar? [S/N]: ')).strip()[0]
    if r in 'Nn':
        break
print(f'{len(pessoas)} pessoas foram cadastradas!')
print(f'Maior peso: {maiorpeso}kg', end='. Peso de ')
for pos, p in enumerate(pessoas):
    if p[1] == maiorpeso:
        print(f'{p[0]}...', end=' ')
print()
print(f'Menor peso: {menorpeso}kg', end='. Peso de ')
for pos, p in enumerate(pessoas):
    if p[1] == menorpeso:
        print(f'{p[0]}...', end=' ')