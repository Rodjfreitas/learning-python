# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha de um jogador, mesmo que algum dado não tenha sido informado corretament


def ficha(nome, gols):
    ficha = {}
    if nome != "":
        ficha['nome'] = nome
    else:
        ficha['nome'] = '<desconhecido>'
    if gols != 0 or gols != "":
        ficha['gols'] = gols
    else:
        ficha['gols'] = 0
    return ficha


nome = str(input('Nome do jogador: ')).strip().title()
while True:
    gols = input('Número de gols: ')
    if gols.isnumeric() == True or gols == "":
        if gols == "":
            gols = 0
        gols = int(gols)
        break
    print('Inválido')
dados = ficha(nome, gols)
print(f'O jogador {dados["nome"]} fez {dados["gols"]} gols no campeonato')
