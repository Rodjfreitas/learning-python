# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome.

nome = str(input('Digite seu nome: ')).strip().title()


if 'Silva' in nome:
    print('Possui Silva no nome')
else:
    print('Não possui Silva no nome')