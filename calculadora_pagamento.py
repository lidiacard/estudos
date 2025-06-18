# EXERCÍCIO: Cálculo de Desconto e Juros para Pagamento
# O programa calcula o valor final de um produto de acordo com a forma de pagamento.
# Se for pago à vista, oferece desconto dependendo da forma de pagamento (cheque/dinheiro ou cartão).
# Se for parcelado, aplica juros de 20% e mostra o valor das parcelas, dependendo do número de vezes.

print(f"{'LOJAS MARIANO':=^40}")
valor = float(input('Qual o valor do produto que deseja comprar? R$'))
pagamento = str(input('O pagamento será á vista ou parcelado? \n[1] Á vista\n[2] Parcelado\n '))

if pagamento == '1':
    pag_avista = input('De qual forma você quer o pagamento à vista? \n[1] Cheque / Dinheiro\n[2] Cartão\n ')
    if pag_avista == '1':
        desconto = 10 / 100 * valor
        print('Com essa forma de pagamento você terá 10% de desconto. O valor', end=' ')
        print(f'ficará de R${valor:.2f} por R${valor - desconto:.2f}')
    else:
        desconto = 5 / 100 * valor
        print('Com essa forma de pagamento você terá 5% de desconto. O valor', end=' ')
        print(f'ficará de R${valor:.2f} por R${valor - desconto:.2f}')
elif pagamento =='2':
    pag_parcelado = input('Em quantas vezes será parcelado?\n[1] Em até 2x\n[2] Em 3x ou mais\n ')
    if pag_parcelado == '1':
        print(f'Você pagará o preço normal de R${valor:.2f}. (2x R${valor/2:.2f})')
    else:
        parc = int(input('Quantas parcelas serão? '))
        juros = 20 / 100 * valor
        valor_juros = valor + juros
        print(f'O valor terá 20% de juros e ficará R${valor_juros:.2f}. ({parc}x R${valor_juros/parc:.2f})')

