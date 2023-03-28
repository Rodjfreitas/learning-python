# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de calculo fatorial
def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for i in range(num, 0, -1): # começa do numero, até o 0, voltando 1.
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i #fatorial recebe fatorial vezes contador
    return f

help(fatorial)
print(fatorial(8, show=True))
