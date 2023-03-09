# O exemplo abaixo é uma estrutura condicional aninhada
nome = str(input('Qual é o seu nome: '))
if nome == 'Rodrigo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in ('Ana Claudia Jessica Juliana'):
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))