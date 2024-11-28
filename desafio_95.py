jogadores = []

while True:
    jogador = {}
    gols = []
    jogador['nome'] = input('Nome do jogador: ')
    while True:
        try:
            partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
            break
        except:
            print('ERRO! Tente novamente.')
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols por partida'] = gols # recebe a lista de gols por partida
    jogador['total'] = sum(gols) # calcula o total de gols
    jogadores.append(jogador.copy())
    while True:
        cont = input('Quer continuar? [S / N] ')[0].upper().strip()
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if cont == 'N':
        break

print(30 * '==')
print(f'{"cod ":<5}{"nome":<15}{"gols":<15}{"total":<6}')
for num, jogador in enumerate(jogadores):
    print(f'{num+1:<5}{jogador["nome"]:<15}{str(jogador["gols por partida"]):<15}{jogador["total"]:<6}')
while True:
    try:
        qual_jogador = int(input('Mostrar dados de qual jogador? (cod) | 999 para parar: '))
    except ValueError:
        print("Por favor, insira um número válido!")
        continue
    if qual_jogador == 999:
        print('<< VOLTE SEMPRE! >>')
        break
    if qual_jogador < 1 or qual_jogador > len(jogadores):
        print(f'ERRO! Não existe jogador com código {qual_jogador}!')
        continue
    for num, jogador in enumerate(jogadores):
        if num+1 == qual_jogador:
            print(30 * '==')
            print(f'-- Levantamento do jogador {jogador['nome']}')
            for p, g in enumerate(jogador['gols por partida']):
                print(f'=> Na partida {p+1}, fez {g} gols.')
            print(f'Foi um total de {jogador['total']} gols')
            print(30 * '==')
