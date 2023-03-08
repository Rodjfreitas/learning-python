# Crie um programa que leia o nome de uma cidade e diga sel ela começa ou não com o nome 'Santo'

cidade = str(input('\nDigite o nome de uma cidade: ')).strip()
# O COMANDO TITLE FOI UTILIZADO PARA PADRONIZAR A ESCRITA INDEPENDENTE DA FORMA QUE O USUÁRIO DIGITAR. PRIMEIRA LETRA MAIUSCULA, DEMAIS MINUSCULAS
cidade = cidade.title()

if 'Santo' in cidade:
    print('\n{} possui Santo no nome.'.format(cidade))
else:
    print('\n{} não possui Santo no nome.'.format(cidade))