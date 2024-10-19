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