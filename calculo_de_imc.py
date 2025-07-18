# EXERCÍCIO: Cálculo do IMC
# O programa calcula o IMC com base no peso e altura da pessoa, e classifica o resultado em faixas:
# 1. Abaixo do peso
# 2. Peso ideal
# 3. Sobrepeso
# 4. Obesidade
# 5. Obesidade mórbida

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)

print(f'{imc:.1f}')

if imc < 18.5:
    print(f'Seu imc é {imc:.1f}. Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é {imc:.1f}. Você está com o peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é {imc:.1f}. Você está com sobrepeso.')
elif imc >= 30 and imc <= 40:
    print(f'Seu imc é {imc:.1f}. Você tem obesidade.')
else:
    print(f'Seu imc é {imc:.1f}. Você tem obesidade mórbida.')