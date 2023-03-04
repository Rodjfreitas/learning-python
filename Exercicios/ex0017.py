from math import hypot,ceil
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjancente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

catetoOposto = float(input('Cateto Oposto: '))
catetoAdjacente = float(input('Cateto Adjacente: '))

print('A hipotenusa do triângulo é {}'.format(ceil(hypot(catetoOposto, catetoAdjacente))))