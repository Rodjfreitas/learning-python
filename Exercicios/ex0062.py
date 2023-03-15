#Melhore o desafio 061 perguntando o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
numeros = []
pa = int(input('Digite a pa: '))
razao = int(input('Digite a razão: '))
i = 0
while i < 10:
    if i == 0:
        numeros.append(pa)
    else:
        pa += razao
        numeros.append(pa)
    i += 1
print('10 primeiros termos da progressão: {}'.format(numeros))
print('{:=^50}'.format('PA'))
opcao = input('Mostrar mais algum termo?\n [1] - sim\n[2] - não\n')
while opcao not in ['1', '2']:
    opcao = input('Mostrar mais algum termo?\n [1] - sim\n[2] - não\n')
while int(opcao) == 1:
    qtd = int(input('Informe quantidade de termos: '))
    pa = int(input('Digite a pa: '))
    razao = int(input('Digite a razão: '))
    numeros = []
    i = 0    
    while i < qtd:
        if i == 0:
            numeros.append(pa)
        else:
            pa += razao
            numeros.append(pa)
        i += 1
    print('{} primeiros termos da progressão: {}'.format(qtd, numeros))
    print('{:=^50}'.format('PA'))
    opcao = input('\nMostrar mais algum termo?\n [1] - sim\n[2] - não\n')
if int(opcao) == 2:
    print('{:=^50}'.format('FIM'))

