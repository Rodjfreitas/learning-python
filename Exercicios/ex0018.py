from math import radians, sin, cos, tan
# Faça um programa que leia um ângulo qualquer e mostre na tela o seno, consseno e tangente desse ângulo.

angulo = int(input('Informe o valor do ângulo: '))

# Encontra o seno,cosseno e tangente. Como o valor de angulo esta em graus, primeiro converte ele em radianos
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O valor de seno é {:.2f}'.format(seno))
print('O valor de cosseno é {:.2f}'.format(cosseno))
print('O valor da tangente é {:.2f}'.format(tangente))