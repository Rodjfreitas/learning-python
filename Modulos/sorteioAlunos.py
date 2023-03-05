import random

alunos = input('\nQuantos alunos possui a turma? ')
while alunos.isdigit() == False or alunos == '0':
    print('\nEntrada Inválida!')
    alunos = input('\nQuantos alunos possui a turma? ')
# Confirmar o Valor digitado
confirmar = int(input(
    '\nVocê confirma que são {} alunos?\n[1] - Sim\n[2] - Não\n'.format(alunos)))
while confirmar < 1 or confirmar > 2:
    print('\nValor inválido')
    confirmar = int(input(
        '\nVocê confirma que são {} alunos?\n[1] - Sim\n[2] - Não\n'.format(alunos)))

if confirmar == 2:
    print('Encerrando aplicativo.Inicie novamente')
else:  

    # Converte o valor digitado acima em números inteiros
    qtdalunos = int(alunos)
    listaAlunos = []
    i = 0
    # Pedir para usuário digitar o nome dos alunos de acordo com a quantidade de alunos informada
    while i < qtdalunos:
        nomealuno = input('Digite o nome do aluno {}: '.format((i+1)))
        while nomealuno.isalnum() == True:
            print('Nome inválido!\n')
            nomealuno = input('Digite o nome do aluno {}: '.format((i+1)))
        listaAlunos.append([nomealuno])
        i += 1


    print('\nO aluno sorteado para apagar o quadro foi o(a): {}\n'.format(random.sample(listaAlunos, 1)))
    print('\nOrdem dos alunos sorteados para apresentação do trabalho:')
    #sorteio de ordem
    i = 0
    sorteioAlunos = random.sample(listaAlunos, qtdalunos)
    while i < qtdalunos:
        print('{}° aluno: {}'.format((i+1), sorteioAlunos[i] ))
        i += 1

    print('\nOrdem Alfabética:\n')
    # ordem alfabética
    ordem = sorted(listaAlunos)
    i = 0
    while i < len(ordem):
        print('{}): {}'.format(i + 1, ordem[i]))
        i += 1
