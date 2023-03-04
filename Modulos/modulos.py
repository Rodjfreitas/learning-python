from math import sqrt, floor
## import math - importa a biblioteca toda
## from math import ceil - importa um elemento da biblioteca
## from math import ceil, floor - importa dois elementos da bibilioteca

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual à {}'.format(num, floor(raiz)))
