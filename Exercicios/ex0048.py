# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
numeros = []
for c in range(1, 501):
    if c % 3 == 0:
        soma += c
        numeros.append(c)
print(
    '\nA soma dos números impares multiplos de três no intervalo de 1 à 500 é igual à \033[1;30;42m{}\033[m.'.format(soma))
print('\nOs números que se enquadram nas exigências acima são: {}'.format(numeros))
