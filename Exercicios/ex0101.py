# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto Negado, Opcional ou obrigatório nas eleições


def voto(nascimento):
    # se necessária somente dentro da função, use sempre dentro.
    from datetime import datetime
    idade = datetime.now().year - nascimento
    if idade < 16:
        return f'com {idade} anos: VOTO NEGADO.'
    elif idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO.'


while True:
    nascimento = input('Em que ano você nasceu? ').strip()
    if nascimento.isnumeric() == True and len(nascimento) == 4:
        nascimento = int(nascimento)
        break
    print('Inválido.')
print(voto(nascimento))
