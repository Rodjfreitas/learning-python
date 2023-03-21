# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogoCompleto = list()
jogada = list()
total = 0
quantidade = int(input('Quantos jogos da Mega-Sena você quer fazer? '))
for c in range(0, quantidade):
    for jogo in range(0, 6):
        valor = randint(1, 61)
        while valor in jogada:
           valor = randint(1, 61) 
        jogada.append(valor)
    jogada.sort()
    jogoCompleto.append(jogada[:])
    jogada.clear()
    total += 4.50
print(f'\nVocê optou por fazer {quantidade} jogos:')
for jogo in jogoCompleto:
    print(f'jogo {jogoCompleto.index(jogo) + 1}: {jogo}')
    sleep(1)
print(f'\nSeus jogos custaram R$ {total:.2f}')
print(f'\n{"Boa Sorte":=^50}')