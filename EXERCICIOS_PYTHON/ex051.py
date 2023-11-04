#Ler o primeiro termo e a razão de uma PA, e mostrar os 10 primeiros termos da progressão
# an = a1 + (n - 1)r ===============
# Onde:
# an é o termo geral da PA
# a1 é o primeiro termo da PA
# n é a posição do termo na PA
# r é a razão da PA


a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))

pa = [a1]
for i in range(1,11):
    an = a1 + i * r
    pa.append(an)
print(f'Os primeiros 10 termos da PA são: {pa}')
