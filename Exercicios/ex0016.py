from math import trunc
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira. ex: digite um número 6.127 O número tem a parte inteira 6.

numero = float(input('Digite um número real: '))
print('O número tem a parte inteira {}'.format(trunc(numero)))