num = [2, 5, 9, 1]
num[3] = 6   #indice 3 da lista passa a ter o valor 6  [2, 5, 9, 6]
num.append(7)   # [2,5,9,6,7]
num.sort()  #coloca a lista em ordem [2,5,6,7,9]
num.sort(reverse=True)  #coloca a lista em ordem contrária [9,7,6,5,2]
num.insert(2,3) #adiciona o número 3 na posição 2 [9,7,3,6,5,2]
num.pop()  #elimina o último valor da lista [9,7,3,6,5]
num.pop(2)  #elimina o elemento da posição 2 [9,7,6,5]
num.insert(2,9) #adiciona o número 9 na posição 2 [9,7,9,6,5]
num.remove(9)  #elimina apenas o PRIMEIRO número 9 [7,9,6,5]
print(num)
print(f'Essa lista tem {len(num)} números')
print('------------------------------------')
valores = list()    #cria lista vazia, mas poderia ser = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)   #[5,9,4]
for v in valores:
    print(f'{v}...', end='') #5...9...4...

for c, v in enumerate(valores):
    print(f'\nNa posição {c} está o valor {v}')

#for cont in range(1,5):
   # valores.append(int(input(f'Digite o {cont}° valor: '))) # [5,9,4,a,b,c,d]
#print(valores)
print('-----------------')
a = [2,3,4,7]
c = a[:]  #C vai receber todos os elementos de A, mas as listas não terão vínculo
b = a  #criou-se uma ligação entre as listas
b[2] = 8   #vai mudar a posição 2 tanto na lista a quanto na b, a = [2,3,8,7] b = [2,3,8,7]
print(f'Lista A: {a}')  # [2,3,8,7]
print(f'Lista B: {b}')  # [2,3,8,7]
print(f'Lista C: {c}')  # [2,3,4,7]
