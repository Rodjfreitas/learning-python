# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Digite um número inteiro: '))

print('A tabuada de {} é: '.format(numero))

i = 0
while i < 11:
    print('{} x {} = {}'.format(numero, i, numero * i))
    i += 1