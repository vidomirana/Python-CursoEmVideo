# Conversor de temperatura

TC = float(input('Digite a temperatura em graus Celsius (apenas número):  '))
TK = TC + 273.15
TF = 32 + (9 * TC / 5)

print(f'A temperatura de {TC}ºC equivale a {TK}K e {TF}ºF')
