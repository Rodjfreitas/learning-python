dado = input('Digite algo: ')

if dado.isnumeric():
    print('Não pode ser números. Digite apenas letras.')
elif dado.isalnum():
    print('Não pode ser alphanumérico. Digite apenas letras')
else:
    print('seu dado é "{}"'.format(dado))
