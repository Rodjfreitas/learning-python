#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
for numero in range(0, 5):
    valores.append(int(input(f'Digite {numero + 1}° valor: ')))
print(f'O maior valor é {max(valores)} nas posições ', end='')
for pos, numero in enumerate (valores):
    if numero == max(valores):
        print(f'...{pos}', end='')
print(f'\nO menor valor é {min(valores)} nas posições ', end='')
for pos, numero in enumerate (valores):
    if numero == min(valores):
        print(f'...{pos}', end='')
