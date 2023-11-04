#Ler nome, idade e sexo de 4 pessoas e :
#Mostrar a média de idade do grupo
#Dizer o nome do homem mais velho
#Dizer quantas mulheres tem menos de 20 anos
somaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'---------{p}ª--------- pessoa')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = (somaidade / 4)
print(f'A média do grupo é de {mediaidade} anos')
print(f'{nomemaisvelho} tem {maioridadehomem} e é o homem mais velho')
print(f'Existem {totmulher20} mulheres com menos de 20 anos no grupo')


