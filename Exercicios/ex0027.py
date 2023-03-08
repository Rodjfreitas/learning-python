# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('\nDigite seu nome completo: ')).strip().title()
nomeSeparado = nome.split()
qtdespacos = len(nomeSeparado) - 1

while qtdespacos < 2:
    nome = str(input('\nInválido. Digite seu nome completo: '))

print('\nSeja bem vindo {} {}'.format(nomeSeparado[0], nomeSeparado[qtdespacos]))
