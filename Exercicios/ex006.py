# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))

print('O dobro do número é {} \nO triplo do número é {} \nA raiz quadrada do número é {:.2f}.'.format(numero * 2, numero * 3, numero ** (1/2)))
