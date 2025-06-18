# EXERCÍCIO: Conversor de Números para Extenso
# Objetivo: O programa permite ao usuário digitar um número entre 0 e 20 e 
# retorna o número por extenso. O processo pode ser repetido até que o usuário
# escolha encerrar.
# 
# Funcionalidades:
# 1. Solicita ao usuário que insira um número entre 0 e 20.
# 2. Exibe o número por extenso.
# 3. O programa continua até o usuário optar por parar.

continuar = 'S'
while continuar == 'S':
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    num_ext = int(input('Digite um número entre 0 e 20: '))
    while num_ext < 0 or num_ext > 20:
        num_ext = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[num_ext]}')
    continuar = input('Quer continuar? [S/N] ')[0].upper().strip()
print('Programa encerrado')