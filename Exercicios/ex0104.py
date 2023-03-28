# Crie um programa que tenha a função chamada leiaint(), que vai funcionar de forma semelhante a função input() do python, só que fazendo a validação para aceitar apenas valor numérico.


def leiaint(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric() == True:
            return valor
        print('\033[0;31mERRO! Digite um número inteiro válido\033[m')


# Programa Principal
n = leiaint('Digite um número: \033[1;32m')
print(f'\033[1;32mVocê acabou de digitar o número {n}\033[m')
