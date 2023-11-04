#Analisar se os parênteses de uma expressão matématica estão na posição correta
expr = str(input('Digite uma expressão matemática: '))
if "(" in expr:
    if expr.count('(') == expr.count(')'):
        if expr.index('(') == expr.index(')') + 1:
            print('A expressão está ERRADA!')
        elif expr.index('(') == expr.index(')') - 1:
            print('A expressão está ERRADA!')
        elif expr.index(')') < expr.index('('):
            print('A expressão está ERRADA!')
        else:
            print('A expressão está CORRETA!')
    else:
        print('A expressão está ERRADA!')
else:
    print('A expressão está CORRETA!')
