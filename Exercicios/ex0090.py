# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
situacao = {}
situacao['nome'] = str(input('Nome: ')).strip().title()
situacao['media'] = float(input(f'Média de {situacao["nome"]}: '))
if situacao['media'] < 5:
    situacao['status'] = 'Reprovado'
elif situacao['media'] < 7:
    situacao['status'] = 'Recuperação'
else:
    situacao['status'] = 'Aprovado'

for k, v in situacao.items():
    print(f'{k} é igual à {v}')
