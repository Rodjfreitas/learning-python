from datetime import datetime
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: a) quantas pessoas foram cadastradas b) a média de idade do grupo c) uma lista com todas as mulheres. d) uma lista com todas as pessoas com idade acima da média
cadastro = []
dados = {}
media = 0
while True:
    # Validação do nome
    while True:
        dados['nome'] = input('Nome Completo: ').strip().title()
        if dados['nome'].count(" ") >= 1:
            break
        print('Nome Inválido. Necessário Digitar nome completo.')
    # Validação do sexo
    while True:
        dados['sexo'] = input('Sexo[M/F]: ').strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Inválido. Digite M para Masculino, F para Feminino')
    # Validação ano de nascimento
    while True:
        nascimento = input('Ano de Nascimento: ').strip()
        if len(nascimento) == 4 and nascimento.isnumeric() == True:
            nascimento = int(nascimento)
            break
        print('Ano de nascimento Inválido.')

    dados['idade'] = datetime.now().year - nascimento
    cadastro.append(dados.copy())
    dados.clear()
    # Validação de Continuação (Sim/Não)
    while True:
        continuar = input('Novo cadastro?[S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('Você deve digitar S para Sim / N para Não')
    if continuar == 'N':
        break
print(cadastro)
print("\n")
print("=-" * 15, end='')
print("Cadastro", end='')
print("=-" * 15)

# Quantidade de Pessoas Cadastradas
if len(cadastro) == 1:
    print(f'Foi cadastrada {len(cadastro)} pessoa.')
    # Média de Idade
    print(f'A média de idade é de {cadastro[0]["idade"]} anos.')
    print("\n")
else:
    print(f'Foram cadastradas {len(cadastro)} pessoas.')
    # Média de Idade
    for pos, v in enumerate(cadastro):
        media += v['idade']
    media = media / len(cadastro)
    print(f'A média de idade das pessoas cadastradas é de {media:.0f} anos.')
    print("\n")

# Cria uma lista de cadastro ordenando os dicionários pela ordem alfabética do nome
cadastroOrdenado = sorted(cadastro, key=lambda dados: dados['nome'])
print("=-" * 10, end='')
print("Mulheres", end='')
print("=-" * 10)
# Identifica as mulheres na lista
for pos, v in enumerate(cadastroOrdenado):
    if v['sexo'] == 'F':
        print(f'{v["nome"]}')
print("\n")


# Quem são as pessoas que possuem idade acima da média
if len(cadastro) > 1:
    print("=-" * 10, end='')
    print("Idade Acima da Média", end='')
    print("=-" * 10)
    for pos, v in enumerate(cadastroOrdenado):
        if v['idade'] > media:
            print(f'{v["nome"]}: {v["idade"]} anos, sexo:{v["sexo"]}')
    print("\n")
