#Mostrar quais são as vogais de cada palavra numa tupla, sem acentos nas palavras
palavras = ('Garrafa', 'Fone', 'Caderno', 'Prateleira', 'Eu', 'Tupla', 'Dividir', 'Navio', 'Urubu')
for palavra in palavras:
    print(f'\n-~-~ A palavra {palavra.upper()} tem as vogais: ', end='')
    for letra in palavra:
        if letra in 'aAeEiIoOuU':
            print(letra, end=' ')
