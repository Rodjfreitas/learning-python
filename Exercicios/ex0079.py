# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso o número já exista dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.
valores = []
for i in range(0, 5):
    valor = int(input(f'Digite o {i + 1}° número: '))
    if valor not in valores:
        valores.append(valor)
valores.sort()
print(f'Os valores únicos são: {valores}')

    