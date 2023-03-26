from time import sleep
# Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior (# Empacotando)


def maior(* numeros):
    sleep(1)
    print("-=" * 40)
    print('Analisando os valores passados....')
    for num in numeros:
        print(f'{num} ', flush=True, end='')
        sleep(1)
    print(f'foram informados {len(numeros)} valores ao todo')
    print(f'O maior valor informado foi {max(numeros)}')
    print("-=" * 40)


maior(5, 10, 17, 20, 13, 8)
maior(6, 5, 1, 9, 3)
maior(2, 6)
