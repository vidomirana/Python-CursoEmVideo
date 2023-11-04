# Cálculo de aluguel de carros

dias = int(input('Por quantos dias o carro foi alugado?  '))
km = float(input('Quantos quilometros o carro rodou?  '))
valor = (60 * dias) + (0.40 * km)

print(f'O valor do aluguel é R${valor:.2f}')
