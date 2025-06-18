# EXERCÍCIO: Jogo de Adivinhação
# O programa gera um número aleatório entre 1 e 10. O usuário tenta adivinhar o número,
# recebendo dicas de "maior" ou "menor" até acertar. O número de tentativas é contado.
# Utiliza as bibliotecas 'random' para gerar o número e 'time' para pausas entre as tentativas.

from random import randint
from time import sleep

num = randint(1, 10)
adivinha = 0
tentativas = 1

while adivinha != num:
    adivinha = int(input('Adivinhe o número entre 1 e 10: '))
    if adivinha == num:
        break
    print('PROCESSANDO...')
    sleep(3)
    if adivinha > 10 or adivinha < 1:
        print('Opção inválida. Digite um número entre 1 e 10.')
        tentativas += 1
        continue
    elif adivinha != num:
        if adivinha < num:
            print('Você errou. É um número maior. Tente novamente.')
        elif adivinha > num:
            print('Você errou. É um número menor. Tente novamente.')
        tentativas += 1
print(f'Você acertou! O número é {num}')
print(f'Palpites necessários: {tentativas}')