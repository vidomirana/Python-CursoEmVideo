#Ler um número e mostrar seu fatorial
n = int(input('Digite um número inteiro: '))
i = 0
fat = 1

while i != n:
    i += 1
    fat = fat * i

print(f'O fatorial de {n} é {fat}')


#print(f'O fatorial de {n} é {fat}')

#numero = int(input("Digite um número inteiro: "))
#fatorial = 1

#for i in range(1, numero+1):
 #   fatorial = fatorial * i

#print("O fatorial de", numero, "é", fatorial)
