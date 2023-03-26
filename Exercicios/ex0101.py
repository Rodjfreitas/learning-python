from datetime import datetime
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto Negado, Opcional ou obrigatório nas eleições


def voto(nascimento):
    idade = datetime.now().year - nascimento
    if idade < 16:
        s = (f'com {idade} anos: VOTO NEGADO.')
    elif idade < 18 or idade > 65:
        s = (f'com {idade} anos: VOTO OPCIONAL.')
    else:
        s = (f'com {idade} anos: VOTO OBRIGATÓRIO.')
    return s


while True:
    nascimento = input('Em que ano você nasceu? ').strip()
    if nascimento.isnumeric() == True and len(nascimento) == 4:
        nascimento = int(nascimento)
        break
    print('Inválido.')
resposta = voto(nascimento)
print(resposta)
