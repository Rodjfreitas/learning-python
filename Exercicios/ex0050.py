# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
soma = 0
numeros = []
for c in range(1, 7):
    numero = int(input('Digite o {}° número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        numeros.append(numero)
print('\nA soma dos números é \033[1;30;42m{}\033[m'.format(soma))
print('\nOs números considerados foram {}'.format(numeros))
    