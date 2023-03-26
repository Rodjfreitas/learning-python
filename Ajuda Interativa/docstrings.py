from time import sleep

# Docstrings


def contador(i=0, f=0, p=0):  # parametros opcionais
    """
    -> Faz uma contagem e mostra na tela.
    :param i: incio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Rodrigo Freitas
    """
    while i <= f:
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
        i += p


contador(2, 2)
help(contador)
