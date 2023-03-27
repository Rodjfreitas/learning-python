# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: a) quantidade de notas b) maior nota c) menor nota d) a média da turma e) a situação (opcional)  Adicione também as docstrings da função


def notas(* num):
    """
    -> Recebe notas escolares para análise de informações
    :param num: numeros (int ou float). Pode-se inserir um número, ou mais de um número separando-os por vírgulas.
    : return: Retorna um dicionário com informações como: total de notas inseridas, a maior e menor nota informada e a média total das notas informadas.
    """
    notas = []
    ficha = {}
    for n in num:
        notas.append(n)
    ficha['total'] = len(notas)
    ficha['menor'] = min(notas)
    ficha['maior'] = max(notas)
    ficha['media'] = sum(notas) / len(notas)
    del notas
    return ficha


help(notas)
resp = notas(5.2, 3.7, 8, 7, 9.1, 1)
print(resp)
