n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

div = n1 / n2
pot = n1 ** 2
pot2 = n2 ** 2

print('A divisão entre os números é de {:.2f} \nA potência de {} é igual à {} \nA potência de {} é igual à {}'.format(div, n1, pot, n2, pot2))

# use \n para quebrar linhas
# use ,end = " " para não quebrar linhas quando usar dois prints


print('A divisão dos números é igual à {:.2f}'.format(div), end=' >>> ')
print('A potência de {} é {}'.format(n1, pot), end=' >>> ')
print('A potência de {} é {}'.format(n2, pot2))