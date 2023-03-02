# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
tintas = (largura * altura) / 2

print('Para pintar sua parede serão necessários {:.0f} lata(s) de tinta'.format(tintas))
