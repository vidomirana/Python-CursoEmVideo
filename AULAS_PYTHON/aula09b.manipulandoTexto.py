frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido)
print(dividido[0]) #mostrar a primeira palavra da frase
print(dividido[2][3]) #mostra a letra de posição 3 da palavra de posição 2, 'Vídeo' ---> 'e'
frase = frase.replace('Python', 'Java')
print(frase)
print('----------------------------------------------')
print("""O Python foi concebido no final de 1989 por 
Guido van Rossum no Instituto de Pesquisa Nacional 
para Matemática e Ciência da Computação (CWI), nos 
Países Baixos, como um sucessor da ABC capaz de tratar
exceções e prover interface com o sistema operacional 
Amoeba através de scripts.)""" ) #Aspas triplas para imprimir um texto longo com parágrafos