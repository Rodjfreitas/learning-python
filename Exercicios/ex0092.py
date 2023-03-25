from datetime import date
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os com idade em um dicionário. Se por acaso a ctps for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
cadastro = {}
cadastro['nome'] = input('Nome: ').strip().title()
nascimento = input('Ano de Nascimento: ').strip()
while len(nascimento) != 4 or nascimento.isnumeric() == False:
    nascimento = input(
        'Ano Inválido. Insira um ano de Nascimento válido: ').strip()
nascimento = int(nascimento)
cadastro['idade'] = date.today().year - nascimento
ctps = input('Carteira de Trabalho (0 não tem): ').strip()
while ctps.isnumeric() == False:
    ctps = input('Inválido. Carteira de Trabalho (0 não tem): ').strip()
ctps = int(ctps)
if ctps != 0:
    cadastro['ctps'] = ctps
    cadastro['contratação'] = int(input('Ano de contratação: '))
    while cadastro['contratação'] < 1900 or cadastro['contratação'] > date.today().year:
        cadastro['contratação'] = int(input('Inválido. Ano de contratação: '))
    cadastro['salario'] = float(input('Salário:R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + \
        (35 - (date.today().year - cadastro['contratação']))
else:
    cadastro['ctps'] = 0
print("-=" * 50)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
