# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos vai pagar? '))
prestacao = valor_casa / (anos * 12)

if prestacao > (30/100) * salario:
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos,', end=' ')
    print(f'o valor da prestação será R${prestacao:.2f}. EMPRESTIMO NEGADO.')
else:
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos,', end=' ')
    print(f'o valor da prestação será R${prestacao:.2f}. EMPRESTIMO APROVADO!')