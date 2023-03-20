# crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista. ja na posição correta de inserção (sem usar o sort()). no final, mostre a lista ordenada na tela.
valores = []
nwvalores = []
# Cria a Lista
for i in range(0, 5):
    valor = int(input(f'Digite o {i + 1}° valor: '))
    valores.append(valor)
# Cria uma nova lista, inserindo a partir do menor valor e excluindo-o da lista anterior
for i in range(0, 5):
    nwvalores.append(min(valores))
    valores.remove(min(valores))
del valores
for valor in nwvalores:
    print(f'{valor} . ', end='')
