nome = input('digite seu nome: ')
while nome.count(' ') < 2:
    nome = input('Inválido. digite seu nome: ')
print(f'Tudo certo {nome}')
