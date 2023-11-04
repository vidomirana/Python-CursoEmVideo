from getpass import getpass
palavra = getpass('Digite a palavra a ser adivinhada: ').upper()
dica = str(input('Escreva a dica: '))
vazio = []
for i in range(len(palavra)):
    vazio.append('_')
for t in range(1, len(palavra) + 2):
    print(dica)
    print(vazio)
    if '_' not in vazio:
        print('PARABÉNS, VOCÊ ACERTOU!')
        break
    tent = str(input(f'Tentativa {t}. Digite uma letra: ')).strip().upper()[0]
    if tent in palavra:
        for p, l in enumerate(palavra):
            if l == tent:
                vazio.pop(p)
                vazio.insert(p,l)
if '_' in vazio:
  print('VOCÊ PERDEU!! ')