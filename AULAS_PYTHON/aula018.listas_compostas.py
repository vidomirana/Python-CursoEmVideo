teste = list()
teste.append('Vitor')
teste.append(23)
galera = list()
#galera.append(teste)  #está criando uma ligação entre as duas estruturas, seria melhor .append(teste[:])
galera.append(teste[:])
teste[0] = 'Élen'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('-=' * 30)
pessoas = [['Vitinho', 23], ['ÉlenJu', 22], ['Derilma', 49], ['Walter', 52]]
print(pessoas)  #[['Vitinho', 23], ['ÉlenJu', 22], ['Derilma', 49], ['Walter', 52]]
print(pessoas[0]) #['Vitinho', 23]
print(pessoas[1][0]) #ÉlenJu
print(pessoas[3][1]) #52
print(pessoas[2:])  #[['Derilma', 49], ['Walter', 52]]
print(pessoas[:2])  #[['Vitinho', 23], ['ÉlenJu', 22]]
for p in pessoas:
    print(p)  #['Vitinho', 23]
              # ['ÉlenJu', 22]
              # ['Derilma', 49]
              # ['Walter', 52]
print('-=' * 40)
for p in pessoas:
    print(p[1])   #23
                  # 22
                  # 49
                  # 52
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')  #Vitinho tem 23 anos de idade
                                               # ÉlenJu tem 22 anos de idade
                                               # Derilma tem 49 anos de idade
                                               # Walter tem 52 anos de idade
print('-=' * 35)
people = []
dados = []
for i in range(3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    people.append(dados[:])   #CÓPIA!!!! [:]
    dados.clear()
print(people)