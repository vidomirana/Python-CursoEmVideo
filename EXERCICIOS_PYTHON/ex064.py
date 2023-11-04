#Ler vários números até ser digitado 999, mostrar quantos números foram digitados e a soma entre eles
s = 0
i = 0
n = 222 #número qualquer apenas para permitir que o loop while comece
while n != 0:
    i += 1
    n = float(input(f'Digite o {i}° número (0 para parar): '))
    s += n
print(f'Você digitou {i - 1} números e a soma entre eles foi {s}')
