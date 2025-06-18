# EXERCÍCIO: Cadastro de pessoas e análise de dados
# O código permite cadastrar pessoas com nome, sexo e idade.
# No final, é exibido:
# - O total de pessoas cadastradas
# - A média de idades
# - O nome das mulheres cadastradas
# - A lista de pessoas com idade acima da média

lista_pessoas = [] 
soma_idades = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: ')[0].upper().strip()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    while True:
        try:
            pessoa['idade'] = int(input('Idade: '))
            break
        except:
            print('Erro! Digite apenas números.')
    soma_idades += pessoa['idade']
    lista_pessoas.append(pessoa.copy())
    while True:
        continuar = input('Quer continuar? [S / N] ')[0].upper().strip()
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print(30 * '=-')
media_idades = soma_idades / len(lista_pessoas)
print(f'1) Ao todo são {len(lista_pessoas)} pessoas cadastradas.')
print(f'2) A média de idade é {media_idades:.0f} anos.')
print(f'3) Mulheres cadastradas: ', end='')

for pessoa in lista_pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print(f'\n4) Pessoas acima da média de idade: ')

for pessoa in lista_pessoas:
    if pessoa['idade'] > media_idades:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n>> PROGRAMA ENCERRADO <<')