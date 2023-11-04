from datetime import datetime
dados = {}
dados['nome'] = str(input('Insira seu nome: '))
dados['ano_nasc'] = int(input('Insira seu ano de nascimento: '))
ano_atual = datetime.now().year
dados['idade'] = ano_atual - dados['ano_nasc']
dados['ctps'] = int(input('CTPS (0 caso não tenha): '))
if dados['ctps'] != 0:
    dados['ano_contr'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['ano_contr'] + 35) - dados['ano_nasc']
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
