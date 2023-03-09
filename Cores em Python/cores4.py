carteira = input('\nQuanto você possui na carteira? ')
while carteira.isnumeric() == False:
    carteira = input('\nValor Inválido!\nQuanto você possui na carteira? ')
carteira = int(carteira)
if carteira > 50:
    print('Você possui R$ {:.2f}, valor {}Aceitável{}'.format(carteira, '\033[30;42m', '\033[m'))
else:
    print('Você possui R$ {:.2f}, valor {}Não Aceitável{}'.format(carteira, '\033[30;41m', '\033[m'))