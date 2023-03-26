def fgtsCalc(salario):
    fgts = salario * 0.08
    return fgts


def vtCalc(salario):
    vt = salario * 0.06
    return vt


def titulo(msg):
    print("=-~" * 15)
    print(f'{msg:^40}')
    print("=-~" * 15)

cadastro = []
while True:
    titulo('Novo Cadastro')    
    dados = {}
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['salario'] = float(input('Digite seu salário: '))
    dados['fgts'] = fgtsCalc(dados['salario'])
    while True:
        optVt = input('Optante de vt?[S/N] ').upper()[0]
        if optVt in 'SN':
            break
        print('Inválido.')
    if optVt == 'S':
        dados['vt'] = vtCalc(dados['salario'])
    else:
        dados['vt'] = 0
    cadastro.append(dados.copy())
    dados.clear()
    titulo('Novo Cadastro?')
    while True:
        novo = input('Novo Cadastro[S/N]: ').upper()[0]
        if novo in 'SN':
            break
        print('Inválido')
    if novo == 'N':
        break
print(f'{"No.":3} {"Nome":30} {"Salario":7} {"FGTS":7} {"VT":7}')
for pos, valor in enumerate(cadastro):
    print(
        f'{pos:>3} {valor["nome"]:30} {valor["salario"]:7.2f} {valor["fgts"]:7.2f} {valor["vt"]:7.2f}')
