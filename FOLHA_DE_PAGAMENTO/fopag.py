from datetime import datetime

ano = datetime.now().year


def titulo(msg):
    print('~' * 30)
    print(f'{msg:^30}')
    print('~' * 30)


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
    return cont


def calcINSS(sal):
    inss = 0
    alqInss = 0
    if sal <= 1100:
        inss += sal * 0.075
        alqInss = 7.5
    elif sal <= 2203.48:
        inss += 1100 * 0.075
        inss += (sal - 1100.01) * 0.09
        alqInss = 9.0
    elif sal <= 3305.22:
        inss += 1100 * 0.075
        inss += (2203.48 - 1100.01) * 0.09
        inss += (sal - 2203.49) * 0.12
        alqInss = 12.0
    elif sal <= 6433.57:
        inss += 1100 * 0.075
        inss += (2203.48 - 1100.01) * 0.09
        inss += (3305.23 - 2203.49) * 0.12
        inss += (sal - 3305.24) * 0.14
        alqInss = 14.0
    return inss


def calcIRRF(sal):
    irrf = 0
    if sal <= 1903.99:
        irrf = 0
    elif sal <= 2826.65:
        irrf = (sal * 0.075) - 142.8
    elif sal <= 3751.05:
        irrf = (sal * 0.15) - 354.8
    elif sal <= 4664.68:
        irrf = (sal * 0.225) - 636.13
    else:
        irrf = (sal * 0.275) - 869.36
    return irrf


cadastro = []
dados = {}
while True:
    titulo('Cadastro')
    while True:
        nome = input('Nome Completo: ').strip().title()
        if nome.count(' ') > 0:
            dados['nome'] = nome
            break
        print(error('Inválido: Nome completo por favor.'))

    while True:
        nascimento = input('Ano de Nascimento: ')
        if int(nascimento) > ano:
            print(error('Inválido. Ano não pode ser maior que o atual.'))
        elif len(nascimento) == 4 and nascimento.isnumeric() == True:
            nascimento = int(nascimento)
            dados['nascimento'] = nascimento
            dados['idade'] = ano - nascimento
            break
        else:
            print(error('Inválido. Ano deve ser completo, ex: 1990.'))

    while True:
        sexo = input('Sexo[M/F]: ').strip().upper()[0]
        if sexo in 'MF':
            dados['sexo'] = sexo
            break
        print(error('Inválido. Digite M para Masculino, F para Feminino'))

    while True:
        salario = input('Salário Bruto: ')
        if salario.isnumeric() == True:
            salario = float(salario)
            dados['salario'] = salario
            break
        print(error('Inválido. Aceito apenas valor numérico.'))

    while True:
        vt = input('Possui  vale Transporte? [S/N]: ').strip().upper()
        if vt in 'SN':
            if vt == 'S':
                vtValor = float(input('Qual valor da passagem? '))
                dados['vt'] = calcVt(vtValor, salario)
            else:
                dados['vt'] = 0.00
            break
        print(error('Inválido. Digite S para Sim e N para Não.'))

    dados['fgts'] = calcFgts(salario)
    dados['inss'] = calcINSS(salario)
    baseIRRF = dados['salario'] - dados['inss']
    dados['irrf'] = calcIRRF(baseIRRF)
    dados['saLiq'] = dados['salario'] - \
        dados['inss'] - dados['irrf'] - dados['vt']

    cadastro.append(dados.copy())
    dados.clear()
    print('\n')

    while True:
        continuar = input('Realizar novo cadastro?[S/N]: ').strip().upper()
        if continuar in 'SN':
            break
        print(error('Inválido. Digite S para Sim e N para Não.'))
    if continuar == 'N':
        break
titulo('Resumo de Folha')

print(f'{"No.":<4}{"Nome":20}{"Nasc.":6}{"Idade":8}{"Sexo":6}{"Salário Bruto":15}{"VT":12}{"FGTS":12}{"INSS":12}{"IRRF":12}{"Salário Líquido":15}')

for pos, valor in enumerate(cadastro):
    print(f'{pos:<4}{valor["nome"]:20}{valor["nascimento"]:<6}{valor["idade"]:<8}{valor["sexo"]:<6}R${valor["salario"]:<13.2f}R${valor["vt"]:<10.2f}R${valor["fgts"]:<10.2f}R${valor["inss"]:<10.2f}R${valor["irrf"]:<10.2f}= R${valor["saLiq"]:<11.2f}')
print('\n')
