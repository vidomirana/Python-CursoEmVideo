#As três retas podem formar qual triângulo?

r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))

sr2r3 = r2 + r3
sr1r3 = r1 + r3
sr1r2 = r1 + r2

if r1 < sr2r3 and r2 < sr1r3 and r3 < sr1r2:
    print('\033[32mFORMAM triângulo')
else:
    print('\033[31mNÃO formam triângulo')

if (r1 < sr2r3 and r2 < sr1r3 and r3 < sr1r2) == True:
    if r1 != r2 and r2 != r3 and r1 != r3:
        print('TRIANGULO ESCALENO')
    elif r1 == r2 == r3:
        print('TRIÂNGULO EQUILÁTERO')
    else:
        print('TRIÂNGULO ISÓSCELES')
