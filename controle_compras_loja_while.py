# EXERCÍCIO: Controle de Compras de Loja
# Objetivo: O programa simula uma loja onde o usuário cadastra produtos com seus valores e:
# 1. Calcula o total da compra.
# 2. Conta quantos produtos custam mais de R$1000,00.
# 3. Identifica o produto mais barato.
# 
# O programa permite o cadastro de múltiplos produtos e termina quando o usuário opta por sair.

print(30 * '-')
print('LOJA YOUGO'.center(30))
print(30 * '-')

somavalores = valormaisbarato = valor = prod_mil = 0
cont = 1
nome_maisbarato = ''

while True:
    produto = input('Nome do produto: ')
    valor = float(input('Valor do produto: R$'))
    if cont == 1 or valor < valormaisbarato:
        valormaisbarato = valor
        nome_maisbarato = produto
    
    somavalores += valor
    if valor > 1000:
        prod_mil += 1
    cont += 1
    continuar =' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break

print('==== FIM DO PROGRAMA ====')
print(' ')
print(f'O total da compra foi R${somavalores:.2f}')
print(f'Temos {prod_mil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {nome_maisbarato} custando R${valormaisbarato:.2f}')
