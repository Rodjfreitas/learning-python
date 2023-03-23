cadastro = []
filme = {}
while True:
    filme['Nome'] = str(input('Digite o nome: ')).strip().title()
    filme['ano'] = ano = int(input('Digite o Nascimento: '))
    while filme['ano'] < 1900 or filme['ano'] > 2023:
        filme['ano'] = int(input('Ano Inválido. Digite o ano do filme: '))
    filme['Estado'] = input('Digite as siglas do Estado: ').strip().upper()
    while len(filme['Estado']) != 2 and filme['Estado'].isalpha() == True:
        filme['Estado'] = input('Inválido. Digite as siglas do Estado: ').strip().upper()
    cadastro.append(filme.copy())

    continuar = input('Continuar[S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Continuar[S/N]: ').upper()
    if continuar == 'N':
        break
print(cadastro)