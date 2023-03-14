# crie um programa que leia dois valores e mostre um menu na tela: somar, multiplicar, maior, novos números, sair do programa. seu programa deverá realizar a operação solicitada em cada caso.

numeros = []
numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite outro número: ')))
print('\nSeja bem vindo ao programa: ')
opcao = input(
    '\nSelecione uma opção:\n[1] - Somar\n[2] - Multiplicar\n[3] - maior\n[4] - Novos números\n[5] - sair do programa\n')
while int(opcao) in [1, 2, 3, 4, 5]:
    opcao = int(opcao)
    if opcao == 1:
        print('A soma dos números informados é: {}'.format(
            numeros[0] + numeros[1]))
        opcao = input(
            '\nSelecione uma opção:\n[1] - Somar\n[2] - Multiplicar\n[3] - maior\n[4] - Novos números\n[5] - sair do programa\n')
    elif opcao == 2:
        print('A multiplicação dos números informados é: {}'.format(
            numeros[0] * numeros[1]))
        opcao = input(
            '\nSelecione uma opção:\n[1] - Somar\n[2] - Multiplicar\n[3] - maior\n[4] - Novos números\n[5] - sair do programa\n')
    elif opcao == 3:
        if numeros[0] > numeros[1]:
            print('Maior número é: {}'.format(numeros[0]))
        else:
            print('Maior número é: {}'.format(numeros[1]))
        opcao = input(
            '\nSelecione uma opção:\n[1] - Somar\n[2] - Multiplicar\n[3] - maior\n[4] - Novos números\n[5] - sair do programa\n')
    elif opcao == 4:
        numeros = []
        numeros.append(int(input('Digite um número: ')))
        numeros.append(int(input('Digite outro número: ')))
        opcao = input(
            '\nSelecione uma opção:\n[1] - Somar\n[2] - Multiplicar\n[3] - maior\n[4] - Novos números\n[5] - sair do programa\n')
    else:
        print('{:=^50}'.format('FIM'))
        break
