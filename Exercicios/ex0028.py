import random
# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
print('\nEste é o jogo do Adivinha. O computador sorteará um número: ')
print('sorteando ...')
print('O número sorteado foi X')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorteado = random.choice(numeros)
chute = input('\nQual número foi sorteado (1 à 9)? ')

while chute.isnumeric() == False or int(chute) < 1 or int(chute) > 9:
    chute = input(
        '\nOps...Você não digitou um número entre 1 e 9.\nVamos tentar novamente:\nQual número foi sorteado (1 à 9)? ')

chute = int(chute)
if chute == sorteado:
    print('\nUauuuu, Parabéns!!! Você acertou na Mosca! Você Venceu!')
else:
    print('\nÓ Nãoooo! você Errou!!!! O computador Venceu!')
print('\nO número sorteado foi {}\n'.format(sorteado))
