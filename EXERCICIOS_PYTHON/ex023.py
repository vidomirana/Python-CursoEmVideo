# Ler um número entre 0 e 9999 e mostrar cada dígito separado
   #ex: 1834                                     1834
        # unidade: 4                    posição: 0123
        # dezena: 3
        # centena: 8
        # milhar: 1

n = str(input('Digite um número entre 0 e 9999: '))
unid = n[3:]
deze = n[2:3]
cent = n[1:2]
mil = n[0]
if len(n) == 4:
    print(f'Unidade: {unid}')
    print(f'Dezena: {deze}')
    print(f'Centena: {cent}')
    print(f'Milhar: {mil}')
if len(n) == 3:
    print(f'Unidade: {n[2]}')
    print(f'Dezena: {n[1]}')
    print(f'Centena: {n[0]}')
if len(n) == 2:
    print(f'Unidade: {n[1]}')
    print(f'Dezena: {n[0]}')
if len(n) == 1:
    print(f'Unidade: {n[0]}')
print('='*30)
#-----Matematicamente------------------------------
n2 = int(input('Digite um número entre 0 e 9999: '))
m = n2 // 1000
c = (n2 % 1000) // 100
d = (n2 % 100) //10
u = (n2 % 10)

print(f' Milhar: {m} \n Centena: {c} \n Dezena: {d} \n Unidade: {u}')