#Classificação campeonato brasileiro 2022
classificacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR',
                 'Atlético-MG', 'Fortaleza', 'São Paulo', 'Botafogo', 'América-MG', 'Santos', 'Goiás',
                 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
#A) Mostrar apenas os 5 primeiros colocados
print(f'Os 5 primeiros colocados são {classificacao[:5]}')
#B) Mostrar os times da zona de rebaixamento
print(f'Os times que estão na zona de rebaixamento são: {classificacao[16:]}')
#C) Mostrar uma lista com os times em ordem alfabética
print(f'Essa é a orden alfabética dos times: {sorted(classificacao)}')
#D) Mostrar a posição de algum time escolhido
time = str(input('Qual time deseja saber a posição? '))
print(f'O {time} está em {classificacao.index(time) + 1}° lugar')