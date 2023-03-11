# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem: - o primeiro valor é maior, - o segundo valor é maior, Não existe valor maior, os dois numeros são iguais.

numeros = []
i = 0
while i < 2:
    num = input('{}) Digite um número inteiro: '.format(i+1))
    while num.isnumeric() == False:
        num = input(
            'Valor inválido: {}) Digite um número inteiro: '.format(i+1))
    num = int(num)
    numeros.append(num)
    i += 1

if numeros[0] == numeros[1]:
    print(
        'Não existe número maior. Ambos são iguais. {} / {}'.format(numeros[0], numeros[1]))
elif numeros[0] > numeros[1]:
    print('O primeiro número ({}) é maior que o segundo número ({}).'.format(
        numeros[0], numeros[1]))
else:
    print('O segundo número ({}) é maior que o primeiro número ({}).'.format(
        numeros[1], numeros[0]))
