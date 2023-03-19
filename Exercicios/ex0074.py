from random import sample
# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
numeros = (sample(range(0, 50), 5))
#maior = 0
#menor = 0
# Método com enumerate
#for pos, numero in enumerate (numeros):
#    if pos == 0:
#        maior = numero
#        menor = numero
#    else:
#        if numero > maior:
#            maior = numero
#        if numero < menor:
#            menor = numero
#print(f'\nOs números sorteados foram: {numeros}')
#print(f'O maior número é {maior} e o menor número é {menor}')
print('Os valores sorteados foram: ', end='')
for numero in numeros:
    print(f'{numero} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}\nO menor valor sorteado foi {min(numeros)}')

