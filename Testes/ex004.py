dado = input('Digite algo: ')

if dado.isnumeric():
    print('Não pode digitar um número')
else:
    print('seu dado é: {}'.format(dado))