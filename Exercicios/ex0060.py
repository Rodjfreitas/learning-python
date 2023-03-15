# Faça um programa que leia um número qualquer e mostre seu fatorial. ex: 5! = 5 * 4 * 3 * 2 * 1 = 120

numero = int(input('Digite um número: '))
multiplicacao = 0
i = 0
while i < numero:
    if i == 0:
        multiplicacao += numero
    else:
        multiplicacao = multiplicacao * (numero - i)
    i += 1    
print('O fatorial de !{} é: {}.'.format(numero, multiplicacao))