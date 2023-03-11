# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria -ate 9 ano mirim, ate 14 anos infantil, ate 19 anos junior, ate 20 anos senior, acima master
nascimento = input('Digite o ano de nascimento: ')
while nascimento.isnumeric() == False or len(nascimento) != 4:
    nascimento = input('Digite o ano de nascimento CORRETO: ')
idade = 2023 - int(nascimento)
if idade <= 9:
    print('sua idade é {} anos. Modalidade: MIRIM'.format(idade))
elif idade <= 14:
    print('sua idade é {} anos. Modalidade: INFANTIL'.format(idade))
elif idade <= 19:
    print('sua idade é {} anos. Modalidade: JUNIOR'.format(idade))
elif idade <= 20:
    print('sua idade é {} anos. Modalidade: SENIOR'.format(idade))
else:
    print('sua idade é {} anos. Modalidade: MASTER'.format(idade))
