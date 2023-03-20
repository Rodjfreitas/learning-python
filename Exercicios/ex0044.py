# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento: 1) a vista dinheiro/cheque 10% 2) a vista cartão 5% 3) em ate 2x no cartao preço normal 4) 3x ou mais no cartão 20% de juros

preco = float(input('Informe preço do produto: R$ '))
pagamento = input(
    'Forma de pagamento:\n[1] - Dinheiro/Cheque à vista\n[2] - Cartão à vista\n[3] - Cartão até 2x\n[4] - Cartão 3x ou mais\n')
while pagamento.isnumeric() == False or int(pagamento) < 1 or int(pagamento) > 4:
    print('\nInválido:')
    pagamento = input(
        'Forma de pagamento:\n[1] - Dinheiro/Cheque à vista\n[2] - Cartão à vista\n[3] - Cartão até 2x\n[4] - Cartão 3x ou mais\n')
pagamento = int(pagamento)

if pagamento == 1:
    preco = preco - (preco * 0.10)
    print('Desconto de 10%. Preço: R$ {:.2f}'.format(preco))
elif pagamento == 2:
    preco = preco - (preco * 0.05)
    print('Desconto de 5%. Preço: R$ {:.2f}'.format(preco))
elif pagamento == 3:
    print('Pagamento do Preço normal: R$ {:.2f}'.format(preco))
else:
    preco = preco + (preco * 0.20)
    print('Juros de 20%. Preço: R$ {:.2f}'.format(preco))
