# Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ele não pode exceder 30% do salario ou então o emprestimo será negado

valor = float(input('Qual Valor da casa? '))
salario = float(input('Digite seu salário? '))
tempo = int(input('Vai pagar em quantos anos? '))

tempo = tempo * 12

financiamento = valor / tempo
limite = salario * 0.30

if financiamento <= limite:
    print('\nSeu emprestimo foi liberado\nValor do Financiamento: R$ {:.2f}\n30% da Renda: R$ {:.2f}'.format(financiamento, limite))
else:
    print('\nNão liberado. O valor do financiamento R$ {:.2f} é maior que os 30% do salário R$ {:.2f}'.format(financiamento, limite))
