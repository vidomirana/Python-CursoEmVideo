distancia = float(input('Qual a distância em km da sua viagem?  '))
curta = distancia * 0.50
longa = distancia * 0.45
if distancia <= 200:
    print(f'Preço da passagem: \033[32mR${curta:.2f}')
else:
    print(f'Preço da passagem: \033[32mR${longa:.2f}')
