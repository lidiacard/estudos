# EXERCÍCIO: Jogo de Par ou Ímpar
# O programa simula um jogo entre o usuário e o computador. O usuário escolhe um número 
# e se decide por "par" ou "ímpar", o computador escolhe outro número aleatório.
# O vencedor é determinado pela soma dos dois números e se o total é par ou ímpar.
# O jogo continua até o usuário perder.

from random import randint
venceu = 0
while True:
    print(15 * '=-')
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print(15 * '=-')
    n = int(input('Diga um valor: '))
    parimpar_jogador = ' '
    while parimpar_jogador not in 'PI':
        parimpar_jogador = input('PAR OU IMPAR? [P/I] ')[0].strip().upper()
    computador = randint(1, 10)
    total = n + computador
    if total % 2 == 0:
        parimpar_pc = 'PAR'
    else:
        parimpar_pc = 'IMPAR'
    print(' ')
    print(f'Você jogou {n} e o computador jogou {computador}. Total de {total}. Deu {parimpar_pc}.')
    print(' ')
    if parimpar_pc[0] == parimpar_jogador:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        venceu += 1
    else:
        print('VOCÊ PERDEU!')
        print(f'GAME OVER! Você venceu {venceu} vezes.')
        break
