# Refaça o desafio 051, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos da progressão usando a estrutura while:
pa = int(input('Digite uma pa inicial: '))
razao = int(input('Digite a razão: '))
numeros = []
i = 0
while i < 10:
    if i == 0:
        numeros.append(pa)
    else:
        pa += razao
        numeros.append(pa)
    i += 1
print('Os dez primeiros termos da progressão são:\n{}'.format(numeros))