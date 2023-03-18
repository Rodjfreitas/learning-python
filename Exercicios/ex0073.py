# Crie uma tupla preenchida com 20 primeiros colocados da tabela do Campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre a) apenas os cinco primeiros colocados. b) os dois ultimos colocados da tabela c) uma lista com os times em ordem alfabética. d) em que posição na tabela está o time da chapecoense.
tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico', 'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América Mineiro', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragrantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético Goianiense', 'Avaí', 'Juventude')
print(f'\n{"Tabela Brasileirão 2022":=^50}\n')

print(f'\n{"Libertadores":=^20}')
for times in range(0, 6):
    print(f'{times + 1}°: {tabela[times]}')
print(f'\n{"Rebaixamento":=^20}')
for times in range(16, 20):
    print(f'{times + 1}°: {tabela[times]}')
print(f'\n{"Ordem Alfabética":=^20}')
for times in sorted(tabela):
    print(f'{times}')
print(f'\n{"Posição":=^20}')
print(f'A posição do Flamento foi {tabela.index("Flamengo") + 1}')
