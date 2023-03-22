# Crie um programa que crie uma matriz de dimensão 3 x 3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela com a formatação correta.
matriz = [[], [], []]
for c in range(0, 3):
    for valor in range(0, 3):
        matriz[c].append(int(input(f'Digite um número para [{c}, {valor}]: ')))
print(f'\n{"MATRIZ 3X3":=^50}\n')
for lista in matriz:
    print(f'[{lista[0]:>4} ] [{lista[1]:>4} ] [{lista[2]:>4} ]')
