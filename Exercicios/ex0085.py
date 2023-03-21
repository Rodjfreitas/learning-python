# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. no final mostre os valores pares e impares em ordem crescente.
numeros = list()
pares = list()
impares = list()
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares.append(valor)        
    else:
        impares.append(valor)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print(f'Pares: {numeros[0]}')
print(f'Ímpares: {numeros[1]}')
print(numeros)