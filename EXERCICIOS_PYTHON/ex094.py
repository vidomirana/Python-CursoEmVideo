#Ler nome, sexo e idade de várias pessoas e guardar num dicionário, cada dicionário em uma lista
#Mostrar o n° de pessoas, média de idade do grupo, n° de mulheres, pessoas com idade acima da média
grupo = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    resp = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'N° de pessoas: {len(grupo)}')
soma_idade = 0
for i in grupo:
    soma_idade += i['idade']
media_idade = soma_idade / len(grupo)
print(f'Média de idade: {media_idade:.2f}')
print(f'As mulheres são: ', end='')
for i in grupo:
    if i['sexo'] == 'F':
        print(i['nome'], end='...')
print()
print('As pessoas com idade acima da média são: ', end='')
for i in grupo:
    if i['idade'] > media_idade:
        print(i['nome'], end='...')

