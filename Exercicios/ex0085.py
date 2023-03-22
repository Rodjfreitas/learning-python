# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. no final mostre os valores pares e impares em ordem crescente.
numeros = [[], []]
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
if len(numeros[0]) != 0:
    print(f'Pares: {numeros[0]}')
else:
    print('Não foram digitados números pares.')
if len(numeros[1]) != 0:
    print(f'Ímpares: {numeros[1]}')
else:
    print('Não foram digitados números ímpares')
