def ordem(lista):
    cadastroOrdem = []
    cadastroOrdem = sorted(lista, key=lambda dados: dados['nome'])
    print(f'{"No.":>3} {"Nome":<20} {"Idade":<5}')
    for pos, valor in enumerate(cadastroOrdem):
        print(f'{pos:>3} {valor["nome"]:<20} {valor["idade"]:>5}')


def titulo(msg):
    print("-=" * 15)
    print(msg)
    print("-=" * 15)


cadastro = [{'nome': 'Rodrigo', 'idade': 35},
            {'nome': 'Natália', 'idade': 35},
            {'nome': 'Alfredo', 'idade': 40}]
titulo('Cadastro')
ordem(cadastro)
novodado = {'nome': 'Marcos', 'idade': 28}
cadastro.append(novodado)
titulo('Cadastro')
ordem(cadastro)
