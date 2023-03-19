#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
for numero in range(0, 5):
    valores.append(int(input(f'Digite {numero + 1}° valor: ')))
print(f'O maior valor é {max(valores)} e seu índice é {valores.index(max(valores))}')
print(f'O menor valor é {min(valores)} e seu índice é {valores.index(min(valores))}')
