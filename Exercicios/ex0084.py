# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# a)quantas pessoas foram cadastradas, b) uma listagem com as pessoas mais pesadas, c) uma listagem com as pessoas mais leves
cadastro = list()
info = list()
while True:
    info.append(str(input('Nome:')))
    info.append(float(input('Peso: ')))
    cadastro.append(info[:])
    info.clear()
    continuar = input('Deseja continuar[S/N]? ').upper()
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]? ').upper()
    if continuar == 'N':
        break
print(f'\nForam cadastradas {len(cadastro)} pessoas.')
maxPeso = 0
for c in cadastro:
    if c[1] > maxPeso:
        maxPeso = c[1]
print(f'O maior peso é {maxPeso} Kg. ', end='')
for pessoa in cadastro:
    if pessoa[1] == maxPeso:
        print(f'{pessoa[0]}, ', end='')
minPeso = maxPeso
for c in cadastro:
    if c[1] < minPeso:
        minPeso = c[1]
print(f'\nO menor peso é {minPeso} Kg. ', end='')
for pessoa in cadastro:
    if pessoa[1] == minPeso:
        print(f'{pessoa[0]}, ', end='')
       