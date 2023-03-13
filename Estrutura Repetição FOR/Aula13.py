inicio = int(input('Digite o início: '))
final = int(input('Digite o final: '))
passo = int(input('Digite o passo: '))

for c in range(inicio, final, passo):
    print('olá n° {}'.format(c))
