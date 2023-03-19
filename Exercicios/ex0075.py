# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os eu uma tupla. No final mostre:a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o primeiro valor 3. quais foram os números pares.
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), 
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Os números digitados foram {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print('Numeros pares: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero}, ', end='')
if 3 in numeros:
    print(f'\nO primeiro valor 3 está na {numeros.index(3) + 1}° posição')
else:
    print('\nNão foram digitados número 3.')

