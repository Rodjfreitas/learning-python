from datetime import date
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: a) quantas pessoas foram cadastradas b) a média de idade do grupo c) uma lista com todas as mulheres. d) uma lista com todas as pessoas com idade acima da média
cadastro = []
dados = {}
media = 0
while True:
    dados['nome'] = input('Nome Completo: ').strip().title()
    while dados['nome'].count(" ") < 1 or dados['nome'].isalnum() == True:
        dados['nome'] = input('Inválido. Nome Completo: ').strip().title()
    dados['sexo'] = input('Sexo[M/F]: ').strip().upper()
    while dados['sexo'] not in 'MF':
       dados['sexo'] = input('Inválido. Sexo[M/F]: ').strip().upper()
    nascimento = input('Ano de Nascimento: ').strip()
    while len(nascimento) != 4 or nascimento.isnumeric() == False:
        nascimento = input('Inválido. Ano de Nascimento: ').strip()
    
    dados['idade'] = date.today().year - int(nascimento)
    cadastro.append(dados.copy())
    dados.clear()
    continuar = input('Novo cadastro?[S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Novo cadastro?[S/N]: ').strip().upper()
    if continuar == 'N':
        break
print(cadastro)
print("\n")
print("=-" * 15, end='')
print("Cadastro", end='')
print("=-" * 15)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
for pos, v in enumerate (cadastro):
    media += v['idade']
media = media / len(cadastro)
print(f'A média de idade das pessoas cadastradas é de {media:.0f} anos.')
print("\n")
print("=-" * 10, end='')
print("Mulheres", end='')
print("=-" * 10)
for pos, v in enumerate (cadastro):
    if v['sexo'] == 'F':
        print(f'{v["nome"]}')
print("\n")
print("=-" * 10, end='')
print("Idade Acima da Média", end='')
print("=-" * 10)
for pos, v in enumerate (cadastro):
    if v['idade'] > media:
        print(f'{v["nome"]}: {v["idade"]} anos, sexo:{v["sexo"]}')
