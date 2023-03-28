# Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. quando o usuário digitar a palavra fim, o programa se encerrará. Obs: use cores.


def ajuda():
    principal = '\033[1;30;42m'
    acessando = '\033[1;30;46m'
    resposta = '\033[7;37;40m'
    fim = '\033[1;30;41m'    
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', principal)
        hp = input('Função ou Biblioteca: ').strip().lower()
        if hp == 'fim':
            titulo('Até logo', fim)
            break
        titulo(f'Acessando o manual do comando "{hp}"', acessando)
        textAjuda(help(hp), resposta)
    




def titulo(msg, cor):
    print(f'{cor}~' * len(msg), f'{cor} ' * 50)
    print(f'{cor}{msg}', f'{cor} ' * 50)
    print(f'{cor}~' * len(msg), f'{cor} ' * 49, '\033[m')


def textAjuda(msg, cor):
    print(f'{cor}{msg}\033[m')


ajuda()