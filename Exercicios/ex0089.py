# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
cadastroCompleto = list()
cadastro = list()
notas = list()
while True:
    cadastro.append(str(input('Nome: ')).strip().title())
    notas.append(int(input('Nota 1) ')))
    notas.append(int(input('Nota 2) ')))
    cadastro.append((notas[0] + notas[1]) / 2)
    cadastro.append(notas[:])
    cadastroCompleto.append(cadastro[:])
    notas.clear()
    cadastro.clear()
    pergunta = input('Quer continuar[S/N]? ').strip().upper()
    while pergunta not in 'SN':
        pergunta = input('Quer continuar[S/N]? ').strip().upper()
    if pergunta == 'N':
        break
print(f'\n{"No.":<3} {"NOME":<20} {"MÉDIA":>10}')
print(f'{"=":=^35}\n')
for valor in cadastroCompleto:
    print(
        f'{cadastroCompleto.index(valor):>3} {valor[0]:<20} {valor[1]}')
print(f'\n{"=":=^35}\n')
print(cadastroCompleto)
while True:
    aluno = int(input('\nMostrar nota de qual aluno? (999 Interrompe): '))
    registros = len(cadastroCompleto)
    while aluno != 999 and aluno + 1 > registros:
        aluno = int(input(
            '\nNão Existe esse aluno.\nMostrar nota de qual aluno? (999 Interrompe): '))
    if aluno == 999:
        print(f'\n{"FIM":=^35}\n')
        break

    print(
        f'Notas de {cadastroCompleto[aluno][0]} são: {cadastroCompleto[aluno][2]}')
