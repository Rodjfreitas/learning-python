# Crie um programa que leia quanto dinheiro uma pessoa  tem na carteira e mostre quantos dólares ela pode comprar:

dinheiro = float(input('Quanto você tem de dinheiro na carteira R$? '))
cotacao = 5.21
conversao = dinheiro * cotacao
conversaoeuro = dinheiro * 5.53

print('com R$ {:.2f} você pode comprar USD$ {:.2f} e/ou  EUR${:.2f}'.format(dinheiro, conversao, conversaoeuro))
