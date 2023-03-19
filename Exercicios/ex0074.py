from random import randint
# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
numeros = (randint(0, 50), randint(0, 50), randint(
    0, 50), randint(0, 50), randint(0, 50))
maior = 0
menor = 0
for pos, numero in enumerate (numeros):
    if pos == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'\nOs números sorteados foram: {numeros}')
print(f'O maior número é {maior} e o menor número é {menor}')
