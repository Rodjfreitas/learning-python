# Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma sequência Fibonacci ex: 0 - 1- 1 - 2 - 3 - 5 - 8    1
print('\n{:=^50}\n'.format('Sequência de Fibonacci'))
print("""Foi a partir de um problema criado por Fibonacci que o mesmo detectou a existência de uma regulariadade matemática.\nTrata-se do exemplo clássico dos coelhos, em que Fibonacci descreve o crescimento de uma população desses animais.\nAssim, começando pelo 1, essa sequência é formada somando cada numeral com o numeral que o antecede.\n""")

numero = 0
opcao = input(
    'Você deseja:\n[1] - Sequência Fibonacci tradicional\n[2] - Criar sua sequência\n[Enter] - Sair\n')
while opcao != "":
    if int(opcao) == 1:
        sequencia = [0, 1]
        numero = int(input('Digite o intervalo da sequência Fibonacci: '))
        i = 0
        while i < numero:
            sequencia.append(sequencia[i] + sequencia[i+1])
            i += 1
        print('A sequência de {} números é {}'.format(numero, sequencia))
        print('\n{:=^50}\n'.format('Nova Sequência de Fibonacci'))
        opcao = input(
            '\nVocê deseja repetir:\n[1] - Sequência Fibonacci tradicional\n[2] - Criar sua sequência\n[Enter] - Sair\n')
    elif int(opcao) == 2:
        sequencia = []
        sequencia.append(int(input('Digite o primeiro número da sequência: ')))
        sequencia.append(sequencia[0] + 1)
        numero = int(input('Digite o intervalo da sequência Fibonacci: '))
        i = 0
        while i < numero:
            sequencia.append(sequencia[i] + sequencia[i+1])
            i += 1
        print('A sequência de {} números é {}'.format(numero, sequencia))
        print('\n{:=^50}\n'.format('Nova Sequência de Fibonacci'))
        opcao = input(
            '\nVocê deseja repetir:\n[1] - Sequência Fibonacci tradicional\n[2] - Criar suasequência\n[Enter] - Sair\n')

print('{:=^50}'.format('FIM'))
