from random import randint
from time import sleep
from operator import itemgetter
# Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esses dicionários em ordem, sabendo que o vencedor tirou o maior número
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'    {k} tirou {v} no dado')
    sleep(1)
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# No exemplo acima a biblioteca operator.itemgetter serve para fazer a ordenação. reverse true é para mostrar primeiro quem tirou os números mais altos
print('Ranking dos jogadores')
for pos, v in enumerate(ranking):
    print(f'    {pos + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
