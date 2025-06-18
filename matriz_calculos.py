# EXERCÍCIO: Matriz 3x3 com Cálculos
# O programa preenche uma matriz 3x3, calcula a soma dos valores pares, 
# a soma dos valores da terceira coluna e o maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somaterceiracoluna = maior_segundalinha = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz [l][c]
        if c == 2:
            somaterceiracoluna += matriz[l][c]
    if matriz[1][l] > maior_segundalinha:
            maior_segundalinha = matriz[1][c]
            
print(30 * '=-')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é: {somapares}')
print(f'A soma dos valores da terceira coluna é: {somaterceiracoluna}')
print(f'O maior valor da segunda linha é: {maior_segundalinha}')