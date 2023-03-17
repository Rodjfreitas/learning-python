from random import randint
jogada = ['Par', 'Impar']
escolhapc = None
vitorias = 0
print(f'{"Par ou Ímpar":=^50}')
while True:
    suaescolha = int(input('\n[0] - Par\n[1] - Ímpar\n'))
    if suaescolha == 0:
        escolhapc = 1
    else:
        escolhapc = 0
    numero = int(input('Digite um número: '))
    numeropc = randint(0, 100)
    print(f'\nVocê escolheu {jogada[suaescolha]} / número {numero}')
    print(f'\nComputador escolheu {jogada[escolhapc]} número {numeropc}')
    soma = numero + numeropc
    if soma % 2 == 0:
        print(f'Soma é PAR: {soma}')
    else:
        print(f'Soma é IMPAR: {soma}')
    if suaescolha == 0 and soma % 2 == 0 or suaescolha == 1 and soma % 2 != 0:
        print('Você Venceu')
        vitorias += 1
        print(f'\n{"Jogar Novamente":=^50}\n')
        soma = 0
    else:
        print('Você perdeu')
        break
print(f'\n{"Resumo":=^50}\n')
print(f'Você venceu {vitorias} partidas')