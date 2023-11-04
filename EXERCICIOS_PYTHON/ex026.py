#crie um programa que leia uma frase e
    #a) Quantas vezes aparece a letra 'a'
    #b) Em que posição ela aparece a primeira vez
    #c) Em que posição ela aparece a última vez

frase_normal = str(input('Digite uma frase: ')).strip()
frase = frase_normal.lower()
contagem = frase.count('a')
comeco = frase.find('a')
inverso = frase[::-1] #inverteu a frase
tamanho_frase = len(frase)
contagem_inversa = inverso.find('a')
ultima = tamanho_frase - contagem_inversa - 1   #poderia usar o .rfind()

if contagem == 0:
    print(f'\033[33mA frase contêm {tamanho_frase} caracteres')
    print(f'\033[34mA letra "a" aparece {contagem} vezes')
else:
    print(f'\033[36mA frase contêm {tamanho_frase} caracteres')
    print(f'\033[97mA letra "a" aparece {contagem} vezes')
    print(f'\033[30mA primeira letra "a" está na posição {comeco} da frase')
    print(f'\033[31mA última letra "a" aparece na posição {ultima} da frase')