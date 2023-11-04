#refazer a tabuada usando laços for
n = int(input('Insira um número: '))
print(f'Tabuada do {n}: ')
print('-=-=' * 4)

for i in range(1,11):
    print(f'{n} x {i} = {n * i}')

print('-=-=' * 4)