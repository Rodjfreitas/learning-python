from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver Pessoas Cadastradas',
                    'Cadastrar Novas pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar um conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção Válida.\033[m')
    sleep(1.5)
