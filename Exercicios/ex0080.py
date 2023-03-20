# crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista. ja na posição correta de inserção (sem usar o sort()). no final, mostre a lista ordenada na tela.
valores = []
nwvalores = []
# Cria a Lista
# for i in range(0, 5):
#    valor = int(input(f'Digite o {i + 1}° valor: '))
#    valores.append(valor)
# Cria uma nova lista, inserindo a partir do menor valor e excluindo-o da lista anterior
# for i in range(0, 5):
#    nwvalores.append(min(valores))
#    valores.remove(min(valores))
# del valores
# for valor in nwvalores:
#    print(f'{valor} . ', end='')

for i in range(0, 5):
    valor = int(input(f'Digite o {i + 1}° valor:'))
    if i == 0:
        valores.append(valor)
        print(f'{valor} adicionado ao final da lista')
    elif valor > max(valores):
        valores.append(valor)
        print(f'{valor} adicionado ao final da lista')
    elif valor < min(valores):
        valores.insert(0, valor)
        print(f'{valor} adicionado a posição 0')
    else:
        x = 1
        while x < 4:
            if valor < valores[x]:
                valores.insert(x, valor)
                print(f'{valor} adicionado a posição {x}')
                break
            x += 1
print(valores)
