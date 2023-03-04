import math
# Faça um programa que leia um ângulo qualquer e mostre na tela o seno, consseno e tangente desse ângulo.

angulo = int(input('Informe o valor do ângulo: '))

# Encontra o seno,cosseno e tangente. Como o valor de angulo esta em graus, primeiro converte ele em radianos
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor de seno é {:.3f}'.format(seno))
print('O valor de cosseno é {:.3f}'.format(cosseno))
print('O valor da tangente é {:.3f}'.format(tangente))