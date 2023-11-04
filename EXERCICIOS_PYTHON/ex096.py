#Criar uma função que calcule a aréa de um terreno
def cabecalho(titulo):
    print('-=' * 30)
    print(f'{titulo:^50}')
    print('-=' * 30)


def area(comprimento, largura):
    a = comprimento * largura
    print(f'Um terreno de dimensões {comprimento} x {largura}m tem uma área de {a:.2f}m²')


cabecalho('CONTROLE DE TERRENO')
area(float(input('Comprimento: ')), (float(input('Largura: '))))
