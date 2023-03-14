from random import randint
# Melhore o jogo do desafio 28 onde o computador vai pensar um número entre 0 10. só que agora o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites foram necessários para vencer.

numero = randint(1, 10)
contagem = 1
print('O computador escolheu um número de 1 à 10. tente adivinha:')
escolha = input('\nQual é o número? ')
while int(escolha) != numero:
    contagem += 1
    escolha = input('\nErrou! Tente novamente: ')
print('\nAcertou. O número escolhido pelo computador foi {}\nVocê precisou de {} tentativas.\n'.format(numero, contagem))
