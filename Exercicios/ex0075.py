# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os eu uma tupla. No final mostre:a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o primeiro valor 3. quais foram os números pares.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))
numero4 = int(input('Digite um número: '))
numeros = (numero1, numero2, numero3, numero4)
cont9 = 0
numerotres = 0
par = 0

for numero in numeros:
    if numero == 9:
        cont9 += 1
    if numero % 2 == 0:
        par += 1
        print(f'{par}° numero par: {numero}')
    if numero == 3:
        numerotres = 'sim'
if numerotres == 'sim':
    print(f'O primeiro número 3 se encontra na posição {numeros.index(3)}')
else:
    print(f'Não foram digitados número 3')
if cont9 > 0:
    print(f'Foram digitados {cont9} vezes o número 9.')
else:
    print(f'Não foram digitados número 9')
if par == 0:
    print(f'Não foram digitados números pares')
