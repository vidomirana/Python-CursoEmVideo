#Refazer o ex051 usando o comando while. 10 primeiros termos de uma PA

a1 = int(input('Qual o primeiro termo da PA?  : '))
r = int(input('Qual a razão da PA? : '))
n = int(input('Quantos números você quer dessa PA? : '))
pa = [a1]
i = 0

while i != n - 1:
    i += 1
    an = a1 + i * r
    pa.append(an)

print(f'Os {n} primeiros elementos dessa PA são {pa}')
decisao = str(input('Quer adicionar mais números? [S/N]: '))
while decisao in 'Ss':
    plus = int(input('Quantos? : '))
    i = 0
    while i != plus:
        i += 1
        anplus = pa[-1] + r
        pa.append(anplus)
    print(f'A PA com os termos adicionados é: {pa}')
    decisao = str(input('Quer adicionar mais números? [S/N]'))
print('Fim.')
