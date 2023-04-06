from lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    return True


def criarArquivo(nome):
    try:
        # wt escreve, + e para o caso de se não existir, ele cria
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
