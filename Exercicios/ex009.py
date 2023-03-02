# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Digite um número inteiro: '))

print('A tabuada de {} é: '.format(numero))
print('{:=^15}'.format('='))
i = 0
while i < 11:
    print('{:^5} x {:^2} = {:<10} - {:<20}'.format(numero, i, (numero * i), ('x' * (numero *i))))
    i += 1

print('{:=^15}'.format('='))