jogador = {}
gols = []

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {p+1}? '))) # lista gols recebe a quantidade de gols por partida
jogador['gols'] = gols
jogador['total'] = sum(gols) # calcula o total de gols

print(30 * '==')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(30 * '==')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for p, g in enumerate(jogador['gols']):
    print(f'  => Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {jogador['total']} gols')