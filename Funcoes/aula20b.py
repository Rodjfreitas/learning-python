def titulo(msg):
    qtd = int(len(msg) / 2)
    print('-=' * qtd)
    print(f'{msg:^}')
    print('-=' * qtd)


titulo('CADASTRO DE FUNCIONÁRIOS')
titulo('MULHERES CADASTRADAS')
titulo('HOMENS CADASTRADOS')