from random import randint
from time import sleep
# Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esses dicionários em ordem, sabendo que o vencedor tirou o maior número no dado.
ranking = {}
for i in range(0, 4):
    ranking[(f'jogador{i + 1}')] = randint(1, 6)

print('Valores sorteados:')
for k, v in ranking.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
rankingOrdenado = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
for pos, v in enumerate(rankingOrdenado):
    print(f'{pos + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
    i += 1
