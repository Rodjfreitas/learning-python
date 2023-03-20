# Crie um programa que vai ler vários números e colocar numa lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas.
valores = []
pares = []
impares = []
quantidade = int(input('Quantos números você deseja digitar? '))
for numero in range(0, quantidade):
    valor = int(input(f'Digite o {numero + 1}° valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
valores.sort()
pares.sort()
impares.sort()
print('\nOs valores são: ', end='')
for valor in valores:
    print(f'{valor} ', end='')
print('\nOs pares são: ', end='')
for valor in pares:
    print(f'{valor} ', end='')
print('\nOs ímpares são: ', end='')
for valor in impares:
    print(f'{valor} ', end='')
