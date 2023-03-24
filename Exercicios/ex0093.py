# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
estatistica = {}
gols = []
total = 0
estatistica['nome'] = input('Nome: ').strip().title()
jogos = int(input(f'Quantas partidas {estatistica["nome"]} jogou? '))
for i in range(0, jogos):
    gols.append(int(input(f'quantos gols na partida {i + 1} ? ')))
    total += gols[i]
estatistica['gols'] = gols[:]
del gols
estatistica['total'] = total
del total
print("=-" * 50)
print(estatistica)
print("=-" * 50)
for k, v in estatistica.items():
    print(f'O campo {k} tem o valor {v}')
print("=-" * 50)
print(f'O jogador {estatistica["nome"]} jogou {jogos} partidas:')
for pos, i in enumerate (estatistica['gols']):
    print(f'    => Na partida {pos + 1}, fez {i} gols.')
print(f'Foi um total de {estatistica["total"]} gols.')
