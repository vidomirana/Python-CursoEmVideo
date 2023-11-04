## Tratamento de strings

nome = 'Vitor Miranda Sousa'
frase = 'VOU COMPRAR PÃO'
frase2 = '   .Aprenda Python.  '
########Vitor Mira n  d  a     S  o  u  s  a
########0123456789 10 11 12 13 14 15 16 17 18

print(nome[0:5]) #mostrar do caractere 0 ao 4º  {não mostra o 5º}
print(nome[14]) #mostra o 14º caractere
print(nome[0:19:2]) #mostra do 0 ao 18º caractere, pulando de 2 em 2
print(nome[:5]) #mostra do caractere 0 ao 4
print(nome[14:]) #mostra do caractere 14 até o final da string
print(nome[6::3]) #mostra do 6 até o final, pulando de 3 em 3
#================================================================

#ANÁLISE DE STRINGS
print(len(nome)) #mostra quantos caracteres a string tem
print(nome.count('a')) #conta quantos 'a' minúsculo tem a string
print(nome.count('a', 0, 13)) #quantos 'a' existem entre o caractere 0 e 12
print(nome.find('usa')) #Mostra a posição onde a sequencia de caracteres começa
print(nome.find('Silva')) #Quando uma sequencia de caracteres não é encontrada, retorna o valor '-1'
print('Vitor' in nome) #Se existir a palavra na string, retorna True, caso contrário, False.
#================================================================

#TRANSFORMAÇÃO DE STRINGS
print(nome.replace('Vitor', 'Jubileu')) #Troca uma palavra por outra
print(nome.upper()) #Coloca letras maiúsculas em toda a string
print(nome.lower()) #Coloca letras minúsculas em toda string
print(frase.capitalize()) #Apenas o primeiro caractere da string fica maiúsculo
print(frase.title()) #Todas palavras terão a primeira letra maiúscula
print(frase2.strip()) #Remove espaços excedentes no ínicio e final da frase
print(frase2.rstrip()) #Remove espaços do lado direito da string
print(frase2.lstrip()) #Remove espaços do lado esquerdo da string
#=================================================================

#DIVISÃO DE STRINGS
print(nome.split()) #Cada palavra da string recebe index novos, além de gerar uma lista contendo cada palavra
                    #que foi dividida ---> 'Vitor' = 0, 'Miranda' = 1, 'Sousa' = 2
#=================================================================

#JUNÇÃO DE STRINGS
print('_'.join(nome.split())) #Juntou as palavras da lista colocando um '_'
print('-'.join(nome)) #Junta todas as letras pelo '-'