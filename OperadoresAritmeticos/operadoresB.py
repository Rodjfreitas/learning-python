numero = int(input('Digite um número: '))

potencia = numero ** 2

if potencia % 2 == 0:
    print('A potência de {} é um Número par = {}'.format(numero, potencia))
else:
    print('A potência de {} é um Número ímpar = {}'.format(numero, potencia))
