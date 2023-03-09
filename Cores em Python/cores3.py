nome = input('\nQual seu nome? ')
qtd = len(nome.split())
while nome.isnumeric() == True:
    nome = input('\nInválido.\nQual seu nome? ')

print('Olá {}{}{}. Prazer em conhecê-lo.'.format('\033[7;36;43m', nome, '\033[m'))