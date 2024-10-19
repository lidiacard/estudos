print('====== BRASILEIRÃO SÉRIE A ======')
tabela = ('Flamengo', 'Botafogo', 'Palmeiras', 'Bahia', 'São Paulo', 'Cruzeiro',
           'Athletico-PR', 'Fortaleza', 'Bragantino', 'Vasco Da Gama', 'Internacional', 
           'Juventude', 'Atlético-MG', 'Criciúma', 'EC Vitória',
           'Cuiabá', 'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense')
print('Os 5 primeiros colocados são:')
for pos, time in enumerate(tabela):
    if pos < 5:
        print(f'{pos+1}ª {time}')
print(' ')

print('Os ultimos 4 colocados são:')
for pos, time in enumerate(tabela):
    if pos > len(tabela) - 5:
        print(f'{pos+1}ª {time}')
print(' ')

print('Times em ordem alfabética:')
print(sorted(tabela))
print(' ')

print(f'O time Juventude está na posição {tabela.index('Juventude') + 1}ª')