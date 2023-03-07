# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um de seus dígitos separados.

numero = input('\nDigite um número de 0 à 9999:\n')

# Verifica se o que foi digitado é número e tem quatro caracteres no máximo
while numero.isnumeric() == False or len(numero) > 4:
    numero = input('\nInválido! Digite um número de 0 à 9999:\n')

digitos = int(len(numero))


if digitos == 4:
    lista = ['milhar', 'centena', 'dezena', 'unidade']
elif digitos == 3:
    lista = ['centena', 'dezena', 'unidade']
elif digitos == 2:
    lista = ['dezena', 'unidade']
else:
    lista = ['unidade']


i = 0
# loop para insersão de numeros de acordo com a quantidade de dígitos informados
while i < digitos:
    print('{}: {}'.format(lista[i], numero[i]))
    i += 1
    
