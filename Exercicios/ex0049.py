# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher. só que agora utilizando um laço for:
numero = int(input('Digite um número: '))
print('{:=^30}'.format(' Tabuada'))
for c in range(0, 11):
    print('{} x {} = {}'.format(numero, c, numero * c))
