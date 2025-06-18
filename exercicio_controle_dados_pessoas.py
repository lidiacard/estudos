# EXERCÍCIO: Análise de Idades e Sexo
# Objetivo: O programa solicita dados de 4 pessoas (nome, idade e sexo) e realiza as seguintes análises:
# 1. Calcula a média de idade das pessoas.
# 2. Identifica o homem mais velho.
# 3. Conta quantas mulheres têm menos de 20 anos.
# 
# Utiliza estruturas de repetição (for) e condicionais (if) para processar os dados.


soma_idade = mais_velho = mulheres_menores = 0

for c in range (1, 5):
    print(f'===== {c}ª PESSOA ====')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    soma_idade += idade
    sexo = input('Sexo [F / M]: ')
    if mais_velho < idade and sexo.upper() == 'M':
        mais_velho = idade
        nome_mais_velho = nome
    if idade < 20 and sexo.upper() == 'F':
        mulheres_menores += 1
media_idade = soma_idade / 4
print(f'A média de idade é {media_idade:.0f} anos')
print(f'O homem mais velho é {nome_mais_velho} e tem {mais_velho} anos')
print(f'Tem {mulheres_menores} mulheres com menos de 20 anos')