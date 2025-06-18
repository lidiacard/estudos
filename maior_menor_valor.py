# EXERCÍCIO: Maior e Menor Valor
# Objetivo: O programa recebe 5 números do usuário, armazena em uma lista e, 
# depois, exibe o maior e o menor valor digitado, além das posições em que 
# esses valores se encontram na lista.

valores = []
maiorvalor = 0
menorvalor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite o {i+1}ª número: ')))
    if i == 0:
        maiorvalor = menorvalor = valores[i]
    else:
        if valores[i] < menorvalor:
            menorvalor = valores[i]
        if valores[i] > maiorvalor:
            maiorvalor = valores[i]
print(40 * '-')
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maiorvalor} nas posições', end=' ')
for v, n in enumerate(valores):
    if n == maiorvalor:
        print(v+1, end='...')
print(f'\nO menor valor foi {menorvalor} nas posições', end=' ')
for v, n in enumerate(valores):
    if n == menorvalor:
        print(v+1, end='...')