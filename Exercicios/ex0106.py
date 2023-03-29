# Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. quando o usuário digitar a palavra fim, o programa se encerrará. Obs: use cores.
from time import sleep

c = ('\033[m)',  # 0 sem cor
     '\033[0;30;41m', # 1 Vermelho
     '\033[0;30;42m', # 2 Verde
     '\033[0;30;43m', # 3 Amarelo
     '\033[0;30;44m', # 4 Azul
     '\033[0;30;45m', # 5 Roxo
     '\033[7;30m'     # 6 Branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[cor], end='')
    sleep(1)


# Programa Principal
comando = ' '
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
titulo('Até Logo', 1)
