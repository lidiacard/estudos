# EXERCÍCIO: Analisador de Triângulos
# Objetivo: O programa verifica se três valores informados podem formar um triângulo 
# e, caso possam, determina o tipo de triângulo (Equilátero, Isósceles ou Escaleno).
# Utiliza as propriedades dos triângulos e condições (if) para classificar os lados.

print('---- ANALISADOR DE TRIÂNGULOS ----')
r1 = float(input('Digite o comprimento do 1ª lado: '))
r2 = float(input('Digite o comprimento do 2ª lado: '))
r3 = float(input('Digite o comprimento do 3ª lado: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Estes lados podem formar um triângulo.')
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('É um triângulo ESCALENO.') #tds os lados são diferentes
    else:
        print('É um triângulo ISÓSCELES.') # dois lados iguais
else:
    print('Estes lados NÃO podem formar um triângulo.')