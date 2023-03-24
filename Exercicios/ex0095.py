# Aprimore o desafio 93 para que funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.
estatisticas = []
dados = {}
temporario = []
gols = 0

while True:
    print(f'\n{"-=":=^10} Cadastro Jogador {"-=":=^10}')
    dados['jogador'] = input('Nome do Jogador: ').strip().title()
    while dados['jogador'].isnumeric() == True:
        dados['jogador'] = input('Inválido. Nome do Jogador: ').strip().title()
    jogos = input(f'Quantos jogos foram disputados por {dados["jogador"]}? ')
    while jogos.isnumeric() == False:
        jogos = input(
            f'Inválido. Quantos jogos foram disputados por {dados["jogador"]}? ')
    for i in range(0, int(jogos)):
        gols += int(input(f'gols marcados no jogo {i + 1}: '))
        temporario.append(gols)
    dados['jogos'] = int(jogos)
    dados['gols'] = temporario[:]
    dados['totalGols'] = gols
    dados['mediaGols'] = gols / int(jogos)
    temporario.clear()
    gols = 0
    estatisticas.append(dados.copy())
    dados.clear()
    continuar = input('Cadastrar novo jogador? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input(
            'Inválido. Cadastrar novo jogador? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
print(estatisticas)
print('-=' * 50)
print(f'{"cod":>3} {"nome":<20} {"jogos":<5} {"Média":<5} {"Total":<5} {"gols":<25}')
for pos, valor in enumerate(estatisticas):
    print(
        f'{pos:>3} {valor["jogador"]:<20} {valor["jogos"]:<5} {valor["mediaGols"]:>5} {valor["totalGols"]:>5} {valor["gols"]}')
while True:
    jogador = int(input('\nMostrar dados de qual jogador? '))
    if jogador > len(estatisticas):
        break
    print(f'Levantamento do jogador {estatisticas[jogador]["jogador"]}')
    for i in range(0, len(estatisticas[jogador]["gols"])):
        print(f'  No jogo {i + 1} fez {estatisticas[jogador]["gols"][i]}')
print(f'{"FIM":=^20}')
