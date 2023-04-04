def aumentar(n, a, formatar=False):
    """
    --> Função de aumento de valores através de porcentagem
    :param n: valor original
    :param a: valor da porcentagem que deseja reajustar. ex 10 para 10% , 5 para 5%.
    :return: retorna o valor de um reajuste desejado em porcentagem
    """
    if formatar:
        return moeda(n + (n * (a / 100)))
    return n + (n * (a / 100))


def diminuir(n, d, formatar=False):
    """
    --> Função de diminuição de valores através de porcentagem
    :param n: valor original
    :param d: valor da porcentagem que deseja reajustar. ex 10 para 10% , 5 para 5%.
    :return: retorna o valor de um reajuste desejado em porcentagem
    """
    if formatar:
        return moeda(n - (n * (d / 100)))
    return n - (n * (d / 100))


def dobro(n, formatar=False):
    if formatar:
        return moeda(n * 2)
    return n * 2


def metade(n, formatar=False):
    if formatar:
        return moeda(n / 2)
    return n / 2


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, a, d):
    print('=' * 50)
    print(f'{"Resumo do Valor":^50}')
    print('=' * 50)
    print(f'{"Preço Analisado:":<28} {moeda(n):>10}')
    print(f'{"Dobro do Preço:":<30} {dobro(n, formatar=True):<10}')
    print(f'{"Metade do Preço:":<30} {metade(n, formatar=True):<10}')
    print(f'{a:4}{"% de aumento:":<26} {aumentar(n, a, formatar=True):<10}')
    print(f'{d:4}{"% de redução:":<26} {diminuir(n, d, formatar=True):<10}')
    print('=' * 50)