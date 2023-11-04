nome = str(input('Qual é seu nome? '))
if nome == 'Vitor':
    print('Nome lindo!!')
elif nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular!')
elif nome in 'Ana Cláudia Élen Juliane':
    print('Belo nome de muié!!')
else:
    print('Seu nome é muito normal')
print(f'Bom dia, {nome}!')