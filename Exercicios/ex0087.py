# Aprimore o desafio anterior, mostrando no final: a) a soma de todos os valores pares digitados, b) a soma dos valores da terceira coluna c) o maior valor da segunda linha
numeros = [[], [], []]
pares = 0
terceira = 0
maior = 0
for c in range(0, 3):
    for valor in range(0, 3):
        numeros[c].append(int(input(f'Digite o valor de [{c}, {valor}]: ')))
for lista in numeros:
    print(f'[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]')

for lista in numeros:
    for valor in lista:
        if valor % 2 == 0:
            pares += valor
        if lista[1] > maior:
            maior = lista[1]
    terceira += lista[2]
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma dos valores da 3° coluna é {terceira}')
print(f'O maior valor digitado na 2° linha é {maior}')

