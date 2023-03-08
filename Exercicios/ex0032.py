# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = input('\nDigite um ano qualquer: ').strip()

while (ano.isnumeric() == False or len(ano) > 4 or len(ano) < 4 or int(ano) == 0):
    ano = input(
        '\nVocê digitou um valor Inválido!\nDigite um ano qualquer (ex: 1988): ').strip()
ano = int(ano)

if ano > 2023:
    tempo = 'será'
elif ano == 2023:
    tempo = 'é'
else:
    tempo = 'foi'

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('{} {} um ano Bissexto.\n'.format(ano, tempo))
else:
    print('{} não {} um ano Bissexto.\n'.format(ano, tempo))
