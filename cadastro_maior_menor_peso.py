# EXERCÍCIO: Cadastro de Pessoas e Identificação dos Maiores e Menores Pesos
# O programa cadastra nome e peso, e identifica as pessoas com maior e menor peso.

dados = []
maispesados = []
maisleves = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    dados.append([nome, peso])

    if len(dados) == 1:
        mai = men = peso
    else:
        if peso > mai:
            mai = peso
        if peso < men:
            men = peso

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

# Identificando as pessoas com maior e menor peso
maispesados = [p[0] for p in dados if p[1] == mai]
maisleves = [p[0] for p in dados if p[1] == men]

print(f'\nForam cadastradas {len(dados)} pessoas.')
print(f'O maior peso foi de {mai}Kg: {", ".join(maispesados)}')
print(f'O menor peso foi de {men}Kg: {", ".join(maisleves)}')