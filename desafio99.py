from time import sleep

def maior(*numeros):
    print(35 * '=')
    maiorvalor = 0
    print('Analisando os valores passados...')
    for num in numeros:
        sleep(0.2)
        print(num, end=' ')
    print(f'\nForam informados {len(numeros)} valores ao todo.')
    print('O maior valor informado foi ', end='')
    for num in numeros:
        if num > maiorvalor:
            maiorvalor = num
    print(maiorvalor)


maior(2, 1, 6, 8, 10, 3)
maior(4, 7, 0)
maior(1, 2)
maior()