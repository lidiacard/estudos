estudantes = {
    'Alice': {'idade': 15, 'notas': [10, 7.0, 8.8]},
    'Júlia': {'idade': 16, 'notas': [9.2, 8.6, 7.0]},
    'José': {'idade': 15, 'notas': [4.5, 7.5, 9.6]}
}

def adicionar_estudante(nome, idade, notas):
    if nome in estudantes:
        print(f'O estudante {nome} já está cadastrado.')
    else:
        estudantes[nome] = {'idade': idade, 'notas': notas}
        print(f'Estudante {nome} cadastrado com sucesso.')

def remover_estudante(nome):
    if nome in estudantes:
        del estudantes[nome]    
        print(f'Estudante {nome} removido com sucesso.')
    else:
        print(f'O estudante {nome} não está cadstrado.')

def atualizar_notas(nome, novas_notas):
    if nome in estudantes:
        estudantes[nome]['notas'] = novas_notas
        print(f'Notas do estudante {nome} atualizadas com sucesso.')
    else:
        print(f'O estudante {nome} não está cadastrado.')

def exibir_informacoes(nome):
    if nome in estudantes:
        info = estudantes[nome]
        print(f'Nome: {nome}, Idade: {info['idade']}, Notas: {info['notas']}')
    else:
        print(f'O estudante {nome} não está cadastrado.')

def calcular_media(nome):
    if nome in estudantes:
        notas = estudantes[nome]['notas']
        media = sum(notas) / len(notas)
        print(f'A média das notas do estudante {nome} é {media:.2f}.')
    else:
        print(f'O estudante {nome} não está cadastrado.')

def menu():
    while True:
        print('Escolha uma opcão:')
        print('1) Adicionar estudante')
        print('2) Remover estudante')
        print('3) Atualizar notas')
        print('4) Exibir informações')
        print('5) Calcular média')
        print('6) Sair')

        opcao = input('Digite a opção desejada:')

        if opcao == '1':
            nome = input('Nome: ')
            idade = input('Idade: ')
            notas = list(map(float, input('Notas (separadas por espaço): ').split()))
            adicionar_estudante(nome, idade, notas)

        elif opcao == '2':
            nome = input('Nome: ')
            remover_estudante(nome)

        elif opcao == '3':
            nome = input('Nome: ')
            novas_notas = list(map(float, input('Novas notas (separadas por espaço): ').split()))
            atualizar_notas(nome, novas_notas)

        elif opcao == '4':
            nome = input('Nome: ')
            exibir_informacoes(nome)

        elif opcao == '5':
            nome = input('Nome: ')
            calcular_media(nome)

        elif opcao == '6':
            break

        else:
            print('Opção inválida. Tente novamente.')

menu()







