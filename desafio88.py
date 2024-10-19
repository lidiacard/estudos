from random import randint
from time import sleep
print(20 * '-')
print('JOGO MEGA SENA'.center(20))
print(20 * '-')
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=- SORTEANDO {jogos} JOGOS -=-=-')
for i in range(0, jogos):
    lista = [] # Inicializa uma nova lista para cada jogo
    while len(lista) < 6:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
        else:
            continue
    lista.sort()
    print(f'Jogo {i+1}: {lista}')
    sleep(1)
print(4 * '=-',' BOA SORTE!', 4 * '=-')