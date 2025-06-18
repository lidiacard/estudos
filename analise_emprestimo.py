# EXERCÍCIO: Empréstimo bancário
# O código simula uma análise de crédito para um empréstimo de financiamento de imóvel.
# Se o valor da prestação for superior a 30% do salário do comprador, o empréstimo é negado.
# Caso contrário, o empréstimo é aprovado.

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