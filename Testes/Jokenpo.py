from time import sleep
from random import randint
jogada = ['Pedra', 'Papel', 'Tesoura']
disputas = 0
venceu = 0
perdeu = 0
empate = 0

jogar = int(input('\nVamos jogar o Jonkenpô?\n[1] - Sim\n[2] - Não\n'))
if int(jogar) == 1:
    escolha = int(
        input('\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n[4] - Sair\n'))
    while escolha > 0 or escolha < 5:
        if escolha == 4:
            break
        suajogada = jogada[escolha - 1]
        escolhaComputer = randint(0, 2)
        computerjogada = jogada[escolhaComputer]
        sleep(1)
        print('Você escolheu: {}\nComputador escolheu: {}'.format(
            suajogada, computerjogada))
        if escolha - 1 == escolhaComputer:
            print('Empate!')
            empate += 1
        elif escolha == 1 and escolhaComputer == 2:
            print('Você Venceu')
            venceu += 1
        elif escolha == 2 and escolhaComputer == 0:
            print('Você Venceu')
            venceu += 1
        elif escolha == 3 and escolhaComputer == 1:
            print('Você Venceu')
            venceu += 1
        else:
            print('Você Perdeu')
            perdeu += 1
        disputas += 1
        print('{:=^50}'.format('Próxima Jogada'))
        escolha = int(
        input('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n[4] - Sair\n'))

else:
    print('\n{:=^50}\n'.format('Fim de Jogo'))
print('\n{:=^50}'.format('Resumo'))
print('Partidas: {}'.format(disputas))
print('Vitórias: {}'.format(venceu))
print('Derrotas: {}'.format(perdeu))
print('Empates: {}'.format(empate))
if venceu > perdeu:
    print('Você foi o grande vencedor!')
elif perdeu > venceu:
    print('Você foi derrotado!')
else:
    print('Tudo igual!')

