def aumentar(n, a):
    """
    --> Função de aumento de valores através de porcentagem
    :param n: valor original
    :param a: valor da porcentagem que deseja reajustar. ex 10 para 10% , 5 para 5%.
    :return: retorna o valor de um reajuste desejado em porcentagem
    """
    return n + (n * (a / 100))


def diminuir(n, d):
    """
    --> Função de diminuição de valores através de porcentagem
    :param n: valor original
    :param d: valor da porcentagem que deseja reajustar. ex 10 para 10% , 5 para 5%.
    :return: retorna o valor de um reajuste desejado em porcentagem
    """ 
    return n - (n * (d / 100))


def dobro(n):
    return n * 2


def metade(n):
    return n / 2