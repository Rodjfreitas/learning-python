from time import sleep
# Faça um programa que tenha uma função chamada contador(), que receba tres parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar tres contagens através da função criada. a) de 1 ate 10 de 1 em 1, de 10 ate 0, de 2 em 2 c) uma contagem personalizada


def contador():
    for i in range(0, 3):
        print("=-" * 20)
        if i == 0:
            inicio = 1
            fim = 10
            passo = 1
        elif i == 1:
            inicio = 10
            fim = 0
            passo = 2
        else:
            print('Agora é sua vez de personalizar a contagem:')
            inicio = int(input('Inicio: '))
            fim = int(input('Fim: '))
            passo = int(input('Passo: '))
        if passo < 0:
            passo = passo * -1
        elif passo == 0:
            passo = 1
        print('Analisando números')
        print("=-" * 20)
        print(f'Contagem de {inicio} à {fim} - de {passo} em {passo}')
        sleep(2.5)
        if inicio < fim:
            while inicio <= fim:
                print(f'{inicio} ', flush=True, end='')
                sleep(0.5)
                inicio += passo
            print(" FIM!")
        else:
            while inicio >= fim:
                print(f'{inicio} ', flush=True, end='')
                sleep(0.5)
                inicio -= passo
            print(" FIM!")


contador()
