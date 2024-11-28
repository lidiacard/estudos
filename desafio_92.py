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