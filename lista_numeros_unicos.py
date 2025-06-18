# EXERCÍCIO: Lista de Números Únicos
# O programa recebe números inteiros do usuário, garantindo que não haja duplicatas.
# A lista final é exibida em ordem crescente após o usuário decidir parar.

numeros = []
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número: '))
    if num in numeros:
        print(f'O número {num} já está na lista')
        continue
    numeros.append(num)
    continuar = input('Deseja acrescentar mais um número? [S/N] ')[0].upper().strip()
numeros.sort()
print(30 * '-')
print(f'Lista de números: {numeros}')
    