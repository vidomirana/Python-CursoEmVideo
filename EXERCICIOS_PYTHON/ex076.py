#Mostrar produtos e seus preços de forma tabular, utilizando só uma tupla
listagem = ('Pão', 3.00, 'Leite', 5.00, 'Queijo', 9.00, 'Presunto', 7.00, 'Mortadela', 4.00, 'Bolo', 14.00)
print('--' * 19)
print(f'{"LISTAGEM DE PREÇOS":^35}')  #melhor centralizar
print('--' * 19)
for pos, produto in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{produto:.<30}R$ {listagem[pos + 1]:>5.2f}')
