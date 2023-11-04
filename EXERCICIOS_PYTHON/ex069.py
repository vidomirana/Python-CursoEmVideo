#Cadastro de várias pessoas e análise
print('-=' * 10)
print('CADASTRO DE PESSOAS')
print('-=' * 10)
i18 = h = m_20 = c = 0
while True:
    while True:
        idade = int(input('IDADE: '))
        if idade >= 18:
            i18 += 1
        if idade >= 0:
            break
    while True:
        sexo = str(input('SEXO [F/M]: ')).strip().upper()[0]
        if sexo == 'M':
            h += 1
        if sexo in 'FfMm':
            break
    if idade < 20 and sexo == 'F':
        m_20 += 1
    while True:
        decisao = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()[0]
        if decisao == 'S':
            break
        if decisao == 'N':
            break
    c += 1
    if decisao == 'N':
        break
print(f'Das {c} pessoas cadastradas:')
print(f'{h} são homens')
print(f'{i18} são pessoas com mais de 18 anos')
print(f'{m_20} são mulheres com menos de 20 anos')
print('-=' * 10, 'PROGRAMA FINALIZADO', '-=' * 10)
