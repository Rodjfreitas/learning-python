# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

comprimentos = []
i = 0
while i < 3:
    comprimento = input('\nDigite o comprimento {}: '.format(i+1)).strip()
    while comprimento.isnumeric() == False or int(comprimento) == 0:
        comprimento = input(
            '\nInválido\nDigite o comprimento {}: '.format(i+1)).strip()
    comprimento = int(comprimento)
    comprimentos.append(comprimento)
    i += 1

if (comprimentos[0] - comprimentos[1]) < comprimentos[2] and (comprimentos[0] + comprimentos[1]) > comprimentos[2]:
    print('\nÉ possível formar um triângulo.\n')
elif (comprimentos[0] - comprimentos[2]) < comprimentos[1] and (comprimentos[0] + comprimentos[2]) > comprimentos[1]:
    print('\nÉ possível formar um triângulo.\n')
elif (comprimentos[1] - comprimentos[2]) < comprimentos[0] and (comprimentos[1] + comprimentos[2]) > comprimentos[0]:
    print('\nÉ possível formar um triângulo.\n')
else:
    print('\nNão é possivel formar um triângulo\n')
