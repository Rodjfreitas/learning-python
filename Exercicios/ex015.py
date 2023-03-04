#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 por dia e 0,15 por km rodado.

km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias? '))

valorTotal = (km * 0.15) + (dias * 60)

print('O valor total do aluguel é de R$ {:.2f}'.format(valorTotal))