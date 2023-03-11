# Faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade: -se ele vai se alistar ao serviço militar - se é hora de se alistar - se ja passou do tempo do alistamento. seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
nome = input('Digite seu nome completo: ').strip()
while len(nome.split()) < 3 or nome.isnumeric == True:
    nome = input('Inválido. Digite seu nome completo: ').strip()
nascimento = input('Digite o ano do seu nascimento: ').strip()
while nascimento.isnumeric == False or len(nascimento) != 4:
    nascimento = input('Inválido. Digite o ano do seu nascimento: ').strip()
nascimento = int(nascimento)
idade = 2023 - nascimento
if idade < 18:
    print('Olá {}. Você se alistara ao Exército Brasileiro daqui há {} ano(s)'.format(nome, 18 - idade))
elif idade > 18:
    print('Olá {}. Você deveria ter se alistao ao Exército Brasileiro há {} ano(s)'.format(nome, idade - 18))
else:
    print('Olá {}. É hora de se alistar ao Exército Brasileiro!'.format(nome))
