# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

numero = input('\nDigite um número qualquer: ').strip()

while numero.isnumeric() == False:
    numero = input('\nVocê digitou um valor Inválido. Só permitido números.\nDigite um número qualquer: ').strip()

numero = int(numero)

if numero % 2 == 0:
    print('\n{} é PAR'.format(numero))
else:
    print('\n{} é IMPAR'.format(numero))