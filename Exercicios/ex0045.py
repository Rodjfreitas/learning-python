import random
# Crie um programa que faça o computador jogar Jokenpô com você.

opcoes = ['Pedra', 'Papel', 'Tesoura']

voce = 0
computador = 0
empates = 0
vezesJogadas = 0

print('{:=^40}'.format('Jokenpô'))
print('\nJokenpô. Vamos competir.')
jogar = input('Você deseja jogar?\n[1] - SIM\n[2] - Não\n')
while jogar.isnumeric() == False or int(jogar) < 1 or int(jogar) > 2:
    jogar = input('\nVamos lá jogador, são duas opções que você pode escolher.\nVocê deseja jogar?\n[1] - SIM\n[2] - Não\n')
while int(jogar) == 1:

    suaEscolha = input('\nEscolha:\n[1] - Pedra  \n[2] - Papel  \n[3] - Tesoura\n').strip()
    while suaEscolha.isnumeric() == False or int(suaEscolha) < 1 or int(suaEscolha) > 3:
        print('\nAjuda aí Jogador... Você possui apenas 3 opções!')
        suaEscolha = input('\nEscolha:\n[1] - Pedra  \n[2] - Papel  \n[3] - Tesoura\n').strip()
    suaEscolha = opcoes[int(suaEscolha) - 1]
    escolhaComputador = random.choice(opcoes)
    print('Você \033[30;43m{}\033[m X \033[30;44m{}\033[m Computador\n'.format(suaEscolha, escolhaComputador))

    if suaEscolha == 'Pedra' and escolhaComputador == 'Tesoura':
        print('\n\033[30;42mVocê Venceu!\033[m\n')
        voce += 1
    elif suaEscolha == 'Tesoura' and escolhaComputador == 'Papel':
        print('\n\033[30;42mVocê Venceu!\033[m\n')
        voce += 1
    elif suaEscolha == 'Papel' and escolhaComputador == 'Pedra':
        print('\n\033[30;42mVocê Venceu!\033[m\n')
        voce += 1
    elif suaEscolha == escolhaComputador:
        print('\n\033[30;43mEmpate\033[m\n')
        empates += 1
    else:
        print('\n\033[30;41mVocê Perdeu!\033[m\n')
        computador += 1
    
    jogar = input('Você deseja jogar novamente?\n[1] - SIM\n[2] - Não\n')
    while jogar.isnumeric() == False or int(jogar) < 1 or int(jogar) > 2:
        jogar = input('\nVamos lá jogador, são duas opções que você pode escolher.\nVocê deseja jogar novamente?\n[1] - SIM\n[2] - Não\n')
    print('{:=^40}'.format('Jokenpô'))
    vezesJogadas += 1

print('Fim de jogo')
print('{:=^20}'.format('Resumo dos jogos'))
print('\nQuantidade de partidas: {}'.format(vezesJogadas))
print('\nVocê {} X {} Computador'.format(voce, computador))
print('\nEmpates: {}'.format(empates))
if voce > computador:
    print('\n\033[30;42mParabéns!!! Você Ganhou!\033[m\n')
elif voce == computador:
    print('\n\033[30;43mNinguém é de Ninguém... O jogo ficou empatado.\033[m\n')
else:
    print('\n\033[30;41mQue feio...Você Perdeu!\033[m\n')
