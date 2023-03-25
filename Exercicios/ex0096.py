# Faça um programa que tenha uma função chamada area(), que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno.
def area(l, c):
    area = float(l * c)
    print(f'A área de um terreno de {l}x{c} possui {area:.1f}m²')


def titulo(msg):
    print("-=" * 20)
    print(f'{msg:^40}')
    print("-=" * 20)


while True:
    titulo('Controle de Terrenos')
    largura = float(input('Informe a largura do terreno: '))
    comprimento = float(input('Informe o comprimento do terreno: '))
    area(largura, comprimento)
    while True:
        continuar = input('\nNovo calculo? [S/N]').upper()[0]
        if continuar in 'SN':
            break
        print('Opção Inválida!')
    if continuar == 'N':
        break
titulo('FIM')
