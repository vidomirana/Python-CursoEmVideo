vel = float(input('Velocidade do carro em km/h: '))
limite = 80
multa_km = 7.00
multa_total = (vel - limite) * multa_km
if vel <= limite:
    print('\033[32mVelocidade dentro do limite')
else:
    print('\033[31mVelocidade acima do limite')
    print(f'Multa de \033[1;31mR${multa_total:.2f}')
