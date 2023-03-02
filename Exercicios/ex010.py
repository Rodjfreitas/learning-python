# Crie um programa que leia quanto dinheiro uma pessoa  tem na carteira e mostre quantos dólares ela pode comprar:

dinheiro = float(input('Quanto você tem de dinheiro? '))
cotacao = 5.21
conversao = dinheiro * cotacao

print('seus R$ {:.2f} equivalem à USD $ {:.2f}'.format(dinheiro, conversao))
