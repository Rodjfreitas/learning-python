# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo sem considerar espaços, quantas letras tem o primeiro nome

nome = input('\nDigite seu nome completo: ')

while nome.isalnum() == True:
    nome = input('\nInválido. Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())
# conta a quantidade total de caracteres digitadas, incluindo espaços
totalcaracteres = len(nome)
totalcaracteres = int(totalcaracteres)
# conta a quantidade de palavras dentro da variavel para que possa identificar a quantidade de espaços
espacos = len(nome.split())
espacos = int(espacos -1)
print('Quantidade de Caracteres: {}'.format(totalcaracteres - espacos))