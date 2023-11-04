# Tinta pra pintar uma parede

a = float(input('Qual a altura da parede em metros?  '))
l = float(input('Qual a largura da parede em metros?  '))
area = a*l
q = area/2
resto = area%2
q2 = (area//2)+1
sobra = q2-q

if resto == 0:
    print(f'A área dessa parede é {area}m² e para pintá-la você precisa de {q:.0f} litros de tinta')
else:
    print(f'A área dessa parede é {area:.2f}m² e para pintá-la você precisa de {q2:.0f} litros de tinta')
    print(f'Sobra {sobra:.2f} litros de tinta')
