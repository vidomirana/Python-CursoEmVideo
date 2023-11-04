#Mostrar os termos da sequencia de Fibonacci

print(10 * '=', 'SEQUÊNCIA DE FIBONACCI', 10 * '=')
n = int(input('Informe quantos números terá a sequência: '))
fibo = [0,1]
if 0 < n <= 1:
    print(f'Sequência de Fibonacci ---> [{fibo[0]}]')
elif 1 < n <= 2:
    print(f'Sequência de Fibonacci ---> {fibo}')
elif n > 2:
    i = 0
    while i != n - 2:
        i += 1
        Fn = fibo[-1] + fibo[-2]
        fibo.append(Fn)
    print(f'Sequência de Fibonacci ---> {fibo}')
    decisao = str(input('Quer adicionar mais termos? [S/N]'))
    while decisao in 'Ss':
        plus = int(input('Quantos? : '))
        i = 0
        while i != plus:
            i += 1
            Fn = fibo[-1] + fibo[-2]
            fibo.append(Fn)
        print(f'Sequência de Fibonacci ---> {fibo}')
        decisao = str(input('Quer adicionar mais termos? [S/N]'))
    print('Fim.')
else:
    print('Valor inválido!')