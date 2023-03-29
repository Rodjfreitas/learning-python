from datetime import datetime

ano = datetime.now().year


def error(msg):
    return f'\033[1;31m{msg}\033[m'


def calcFgts(sal):
    valor = sal * 0.08
    return valor


def calcVt(val, sal):
    mensal = (val * 2) * 30
    cont = sal * 0.06
    if mensal < cont:
        return mensal
    else:
        return cont


cadastro = []
while True:
    dados = {}
    while True:
        nome = input('Nome Completo: ').strip().title()
        if nome.count(' ') > 0:
            dados['nome'] = nome
            break
        print(error('Inválido'))
    while True:
        nascimento = input('Ano de Nascimento: ')
        if len(nascimento) == 4 and nascimento.isnumeric() == True:
            nascimento = int(nascimento)
            dados['nascimento'] = nascimento
            dados['idade'] = ano - nascimento
            break
        print(error('Inválido'))
    while True:
        salario = input('Salário: ')
        if salario.isnumeric() == True:
            salario = float(salario)
            dados['salario'] = salario
            break
        print(error('Inválido'))
    while True:
        vt = input('Possui  vale Transporte? [S/N]').strip().upper()
        if vt in 'SN':
            if vt == 'S':
                vtValor = float(input('Qual valor da passagem? '))
                dados['vt'] = calcVt(vtValor, salario)
            break
        print(error('Inválido'))
    dados['fgts'] = calcFgts(salario)
    print(dados)
