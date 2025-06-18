# EXERCÍCIO: Cadastro de Pessoa e Cálculo de Aposentadoria
# Objetivo: O programa realiza o cadastro de uma pessoa, coletando informações como:
# 1. Nome, idade e CTPS (Carteira de Trabalho e Previdência Social).
# 2. Se a pessoa tem CTPS, o programa também solicita o ano de contratação e o salário.
# 3. Calcula a idade de aposentadoria com base na regra de 35 anos de contribuição.
# 
# O programa exibe todas as informações cadastradas ao final.

from datetime import datetime

pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('CTPS (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['idade aposentadoria'] = (35 - (datetime.now().year - pessoa['ano de contratação'])) + pessoa['idade']

for k, v in pessoa.items():
    print(f'{k}: {v}')