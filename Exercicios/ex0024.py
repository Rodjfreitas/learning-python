# Crie um programa que leia o nome de uma cidade e diga sel ela começa ou não com o nome 'Santo'

cidade = str(input('Digite o nome de uma cidade: '))

if 'Santo' in cidade:
    print('cidade: {} possui Santo no nome.'.format(cidade))
else:
    print('cidade: {} não possui Santo no nome.'.format(cidade))