lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #Tuplas não necessitam de parênteses mais
#Tuplas são imutáveis
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print('================')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f'Comi {len(lanche)} coisas')
print('=================')
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('=================')
for pos, comida in enumerate(lanche):
    print(f'{comida} está na posição {pos}')
print('=================')
print(sorted(lanche)) #Organiza em ordem

