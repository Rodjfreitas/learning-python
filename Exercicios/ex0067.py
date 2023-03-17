# Faça um programa que mostre a tabuada de várias números, um de cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negatívo.
while True:
    numero = int(input('\nQuer ver a tabuada de qual valor? '))
    print(f'{"=":=^50}')
    if numero < 0:
        print(f'\n{"FIM":=^50}\n')
        break
    i = 0
    while i < 11:
        print(f'{numero} x {i} = {numero * i}')
        i += 1
    print(f'{"=":=^50}')
