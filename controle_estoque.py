# EXERCÍCIO: Controle de estoque de produtos
# Este programa gerencia um estoque de produtos, permitindo:
# - Adicionar e remover produtos
# - Atualizar quantidade e preço
# - Exibir informações sobre um produto
# - Mostrar o inventário completo
# - Calcular o valor total do estoque
# O menu oferece as opções de interação com o sistema.

import os

produtos = {
    'arroz': {'quantidade': 5, 'preço': 5.50},
    'feijão': {'quantidade': 7, 'preço': 7.40},
    'água': {'quantidade': 10, 'preço': 2.50}
}

def adicionar_produto(nome, quantidade, preco):
    produtos[nome] = {'quantidade': quantidade, 'preço': preco}

def remover_produto(nome):
    if nome in produtos:
        del produtos[nome]
    else:
        print('Produto não cadastrado.')

def atualizar_quantidade(nome, nova_quantidade):
    if nome in produtos:
        produtos[nome]['quantidade'] = nova_quantidade
        print('Quantidade atualizada.')
    else:
        print('Produto não cadastrado.')
    
def atualizar_preco(nome, novo_preco):
    if nome in produtos:
        produtos[nome]['preço'] = novo_preco
        print('Preço atualizado.')
    else:
        print('Produto não cadastrado.')
    
def exibir_informacoes(nome):
    if nome in produtos:
        info = produtos[nome]
        print(f'Produto: {nome}, Quantidade: {info["quantidade"]}, Preço: R${info["preço"]:.2f}')
    else:
        print('Produto não cadastrado.')

def exibir_inventario():
    if not produtos:
        print('Sem produtos cadastrados.')
    else:
        for produto, info in produtos.items():
            print(f'Produto: {produto:>7}, Quantidade: {info['quantidade']:>2}, Preço: {info['preço']:5.2f}')

def valor_total():
    total = 0
    for nome in produtos:
        total += produtos[nome]['quantidade'] * produtos[nome]['preço']
    print(f'O valor total do estoque é R${total:.2f}')

def menu():
    while True:

        print('1) Adicionar produto')
        print('2) Remover produto')
        print('3) Atualizar quantidade')
        print('4) Atualizar preço')
        print('5) Exibir informações de um produto')
        print('6) Exibir inventario')
        print('7) Exibir valor total do estoque')
        print('8) Sair')  
        opcao = input('Digite a opção desejada: ')
        os.system('cls')

        if opcao == '1':
            nome = input('Nome do produto: ')
            quantidade = int(input('Quantidade: '))
            preco = float(input('Digite o preço: '))
            adicionar_produto(nome, quantidade, preco)

        if opcao == '2':
            nome = input('Nome do produto: ')
            remover_produto(nome)

        if opcao == '3':
            nome = input('Nome do produto: ')
            nova_quantidade = int(input('Nova quantidade: '))
            atualizar_quantidade(nome, nova_quantidade)

        if opcao == '4':
            nome = input('Nome do produto: ')
            novo_preco = float(input('Digite o novo preço: '))
            atualizar_preco(nome, novo_preco)

        if opcao =='5': 
            nome = input('Digite o nome: ')
            exibir_informacoes(nome)

        if opcao == '6':
            exibir_inventario()

        if opcao == '7':
            valor_total()

        if opcao == '8':
            break

menu()

