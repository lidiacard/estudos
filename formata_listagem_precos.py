# EXERCÍCIO: Listagem de Preços
# Objetivo: O programa cria uma lista de produtos com seus respectivos preços.
# Em seguida, exibe esses itens em formato organizado, com os nomes à esquerda 
# e os preços formatados à direita.
#
# Funcionalidades:
# 1. Define uma lista com produtos e seus preços.
# 2. Exibe essa lista de maneira formatada, mostrando os preços com 2 casas decimais.

listagem = ('Frango', 30, 'Leite', 10.45, 'Carne', 34.50, 'Arroz', 31, 'Queijo', 15.34)
print(37 * '-')
print('LISTAGEM DE PREÇOS'.center(37))
print(37 * '-')

for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>5.2f}')
print(37 * '-')
