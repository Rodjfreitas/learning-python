# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de calculo fatorial
def fatorial(num=1, show=False):
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if i == 1:
            mostrar = print(f'{i} = ', end='')
            break
        mostrar = print(f'{i} x ', end='')


    if show==False:
        return mostrar
    return f


print(fatorial(8, False))
