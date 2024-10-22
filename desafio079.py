"""Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

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
    