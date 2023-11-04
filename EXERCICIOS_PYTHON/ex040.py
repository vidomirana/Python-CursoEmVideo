##clássico da média
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >= 5:
    print(f'Sua média é {media:.2f} e você está aprovado!')
else:
    print(f'Sua média é {media:.2f} e você está reprovado!')
