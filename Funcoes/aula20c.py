def soma(a, b):
    soma = a + b
    print(f'A soma de {a} com {b} é igual à {soma}')
    print('\n')


def mensagem(msg):
    print('=-' * 20)
    print(f'{msg:^40}')
    print('=-' * 20)


# Programa Principal
while True:
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    soma(num1, num2)
    while True:
        cont = input('Continuar: [S/N]').upper()[0]
        if cont in 'SN':
            break
        print('Você digitou um valor inválido. digite apenas S/N.')
    if cont == 'N':
        break
mensagem('FIM')
