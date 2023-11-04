#ler o nome de uma pessoa e mostrar:
    # a) O nome completo em maiúsculas
    # b) O nome completo em minúsculas
    # c) Quantas letras tem, sem considerar os espaços
    # d) Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
tamanho_total = len(''.join(nome.split()))
dividido = nome.split()
tam_primeiro_nome = len(dividido[0])
print(f'NOME EM MAIÚSCULAS: {nome.upper()}')
print(f'nome em minúsculas: {nome.lower()}')
print(f'Tamanho do primeiro nome: {tam_primeiro_nome}')
print(f'Tamanho total: {tamanho_total}')

