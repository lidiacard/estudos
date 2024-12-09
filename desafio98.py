from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        print('Impossível contar de 0 em 0!')
        passo = 1 # define o passo como 1 se o valor digitado for 0
    if passo < 0:
        print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio > fim and passo > 0:
            passo = -passo
    for cont in range(inicio, fim + (1 if passo > 0 else -1), passo):
        sleep(0.3)
        print(cont, end=' ')
    print('FIM!')
    print(30 * '=-')


print(30 * '=-')
contador(1, 10, 1)
 
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
while True:
    try:
        inicio = int(input('Início: '))
        fim = int(input('Fim: '))
        passo = int(input('Passo: '))
        contador(inicio, fim, passo)
        break
    except ValueError:
         print('Por favor, digite um número válido! ')