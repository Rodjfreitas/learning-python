import random
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

sorteio = random.sample(numeros, 6)
print('\nOrdem de sorteio original: {}'.format(sorteio))
# sorted coloca em ordem os elementos de uma array
print('\nOrdem numérica do sorteio: {}'.format(sorted(sorteio)))

pares = 0
impares = 0
i = 0
while i < len(sorteio):
    if sorteio[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1


print('\n{} números pares.\n{} números impares\n'.format(pares, impares))

posicaoPar = []
posicaoImpar = []
i = 0
while i < len(sorteio):
    if sorteio[i] % 2 == 0:
        posicaoPar.append(i)
    else:
        posicaoImpar.append(i)
    i += 1

print('\nPosição dos números de acordo com sorteio original:')
print('\nA posição dos números pares: {}.\nA posição dos números ímpares: {}.\n'.format(posicaoPar, posicaoImpar))