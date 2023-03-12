# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número: '))
cont = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        cont += 1
if cont == 2:
    print('{} é um número primo.'.format(numero))
else:
    print('{} não é um número primo.'.format(numero))
