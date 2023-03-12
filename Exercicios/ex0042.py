# Refaça o desafio 35 do triangulos acrescentando o recurso de mostrar que tip de triangulo será formado: - Equilátero: todos os lados iguais, Isósceles: dois lados iguais, Escaleno: todos os lados diferentes

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



