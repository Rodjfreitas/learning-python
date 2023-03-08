# Desenvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas

km = input('\nQual a distância que será percorrida na viagem: ').strip()
while km.isnumeric() == False or int(km) == 0:
    print('\nVocê digitou um valor Inválido.')
    km = input('Qual a distância que será percorrida na viagem: ').strip()
km = int(km)
if km > 200:
    valor = km * 0.45
else:
    valor = km * 0.50
print('\nO valor da passagem será de R$ {:.2f}'.format(valor).replace('.', ','))