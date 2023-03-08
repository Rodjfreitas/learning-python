# Faça um programa que leia tres números e mostre qual é o maior e qual é o menor:

numeros = []

i = 0
while i < 3:
    numero = input('\nDigite o número n°{}: '.format(i+1)).strip()
    while numero.isnumeric() == False:
        numero = input('\nInválido!Digite NOVAMENTE o número n°{}: '.format(i+1)).strip()
    numeros.append(int(numero))
    i += 1

menor = None
maior = None

if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
    maior = numeros[0]
    if numeros[1] < numeros[2]:
        menor = numeros[1]
    else:
        menor = numeros[2]
elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
    maior = numeros[1]
    if numeros[0] < numeros[2]:
        menor = numeros[0]
    else:
        menor = numeros[2]
elif numeros[2] > numeros[0] and numeros[2] > numeros[1]:
    maior = numeros[2]
    if numeros[0] < numeros[1]:
        menor = numeros[0]
    else:
        menor = numeros[1]

print('\nMenor Número: {}\nMaior Número: {}\n'.format(menor, maior))