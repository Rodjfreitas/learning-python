from time import sleep
# Faça um programa que tenha uma função chamada contador(), que receba tres parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar tres contagens através da função criada. a) de 1 ate 10 de 1 em 1, de 10 ate 0, de 2 em 2 c) uma contagem personalizada
def contador():
    for i in range(0, 3):
        if i == 0:
            print("=-" * 15)
            print('Contagem de 1 à 10 de 1 em 1')
            comeco = 1
            final = 11
            pulo = 1
            while comeco < final:
                print(f'{comeco} ', flush=True, end='')
                sleep(0.4)
                comeco += pulo
            print('\n')
        elif i == 1:
            print("=-" * 15)
            print('Contagem de 10 à 0 de 2 em 2')
            comeco = 10
            final = 0
            pulo = 2
            while comeco >= final:
                print(f'{comeco} ', flush=True, end='')
                sleep(0.4)
                comeco -= pulo
            print('\n')
        else:
            print("=-" * 15)
            print('Agora é sua Vez de personalizar a contagem!')
            inicio = int(input('Inicio: '))
            fim = int(input('Fim: '))
            passo = int(input('Passo: '))
            if passo < 0:
                passo = passo * -1
            elif passo == 0:
                passo = 1
            if inicio < fim:
                while inicio < fim:
                    print(f'{inicio}... ', flush=True, end='')
                    sleep(0.4)
                    inicio += passo
                print('\n')
            else:
                while inicio >= fim:
                    print(f'{inicio}... ', flush=True, end='')
                    sleep(0.4)
                    inicio -= passo
                print('\n')


contador()
