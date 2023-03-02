# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1

print('Você digitou {}'.format(numero), end=' > ')
print('Seu antecessor é {}'.format(antecessor), end=' > ')
print('Seu sucessor é {}.'.format(sucessor))