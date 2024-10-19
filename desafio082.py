numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Quer continuar?[S/N] ')[0].upper().strip()
    if resp == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Números lidos: {numeros}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')