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
