# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantos cédulas de cada valor serão entregues. Considere que o caixa possui cédulas de R$ 50, 20 e 10 e 1.
cedulas = [50, 20, 10, 1]
quantidade = [0, 0, 0, 0]
total = 0
notas = ['cinquenta', 'vinte', 'dez', 'um']
print(f'\n{"Banco do Rodrigo":=^50}\n')
valor = int(input('Quanto você quer sacar? R$ '))
i = 0
while i < 4:
    if valor % cedulas[i] == 0:
        quantidade[i] = valor / cedulas[i]
        quantidade[i] = int(quantidade[i])
        total += quantidade[i]
        break
    if valor < valor % cedulas[i]:
        i += 1
    quantidade[i] = valor / cedulas[i]
    quantidade[i] = int(quantidade[i])
    total += quantidade[i]
    valor -= valor - (valor % cedulas[i])
    i += 1
print(f'\n{"Extrato":=^50}\n')
print(f'\ndisponibilizadas {total} cédulas ao total, sendo:\n')
i = 0
while i < 4:
    if quantidade[i] != 0:
        print(f'{quantidade[i]} cédulas de R$ {cedulas[i]:>2},00')
    if i == 3:
        print(f'\n{"FIM":=^50}\n')
    i += 1
