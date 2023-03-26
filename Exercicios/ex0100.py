from random import randint
from time import sleep
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior


def sorteia(lista):
    print('Sorteando 5 valores: ', end='')
    for i in range(0, 5):
        i = randint(0, 10)
        while i in lista:
            i = randint(0, 10)
        lista.append(i)
        print(f'{i} ', flush=True, end='')
        sleep(0.6)
    print('  PRONTO!')
    lista.sort()


def somaPar(lista):
    somar = 0
    for i in lista:
        if i % 2 == 0:
            somar += i
    print(f'A soma dos valores pares de {lista} é:  {somar}')


numeros = []
sorteia(numeros)
somaPar(numeros)
