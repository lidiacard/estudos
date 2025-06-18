# EXERCÍCIO: Jogo de Pedra, Papel e Tesoura
# O programa simula um jogo de Pedra, Papel e Tesoura entre o usuário e o computador.
# O jogador escolhe uma das opções, o computador escolhe aleatoriamente, e o resultado
# (vitória, derrota ou empate) é exibido com base nas regras do jogo.
# A escolha do jogador é comparada com a do computador e o vencedor é determinado.

import random
from time import sleep
VERDE = '\033[32m'
VERMELHO = '\033[31m'
AZUL = '\033[34m'
RESET = '\033[0m'

jogador = input('Escolha uma opção:\nPEDRA\nPAPEL\nTESOURA\n')
computador = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(computador)

print(f'{VERDE}JO')
sleep(0.7)
print(f'{VERMELHO}KEN')
sleep(0.7)
print(f'{AZUL}PO!!{RESET}')
sleep(0.7)
print(25 * '-=')
if jogador.upper() == 'PEDRA' and computador == 'TESOURA':
    print('Você escolheu PEDRA e eu TESOURA. Você venceu!')
elif jogador.upper() == 'PAPEL' and computador == 'PEDRA':
    print('Você escolheu PAPEL e eu PEDRA. Você venceu!')
elif jogador.upper() == 'TESOURA' and computador == 'PAPEL':
    print('Você escolheu TESOURA e eu PAPEL. Você venceu!')
elif jogador.upper() == computador:
    print(f'Você escolheu {jogador.upper()} e eu {computador}. Deu EMPATE!')
elif jogador.upper() not in computador:
    print(f'{VERMELHO}>> OPÇÃO INVÁLIDA <<{RESET}')
else:
    print(f'Você escolheu {jogador.upper()} e eu {computador}. Você perdeu!')
print(25 * '-=')
