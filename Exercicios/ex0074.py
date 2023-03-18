from random import randint
# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
numeros = (randint(0, 50), randint(0, 50), randint(
    0, 50), randint(0, 50), randint(0, 50))
maior = 0
menor = 0
for numero in range(0, len(numeros)):
    if numero == 0:
        maior = numeros[numero]
        menor = numeros[numero]
    else:
        if numeros[numero] > maior:
            maior = numeros[numero]
        if numeros[numero] < menor:
            menor = numeros[numero]

print(f'\nOs números da sorteados foram: {numeros}')
print(f'O maior número é {maior} e o menor número é {menor}')
