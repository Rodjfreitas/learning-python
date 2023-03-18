quantidade = homens = mulheres = maisdezoito = menosvinte = 0

while True:
    print(f'\n{"Pesquisa":=^50}\n')
    # pergunta o sexo
    sexo = str(input('\nDigite o sexo [M/F]\n')).strip().upper()
    # refaz a pergunta se digitar um valor diferente de m/f
    while sexo not in ["F", "M"]:
        sexo = str(input('\nDigite o sexo [M/F]')).strip().upper()
    if sexo == 'M':
        homens += 1
    else:
        mulheres += 1
    # pergunta a idade
    idade = input('\nDigite a idade: ')
    # refaz a pergunta se não digitar um valor numérico
    while idade.isnumeric() == False:
        idade = input('\nDigite a idade: ')
    if int(idade) > 18:
        maisdezoito += 1
    if int(idade) < 20 and sexo == 'F':
        menosvinte += 1
    quantidade += 1
    # pergunta se quer continuar
    continuar = int(input('\nContinuar? \n[1] - Sim   \n[2] - Não\n'))
    # refaz a pergunta se digitar um valor diferente do permitido
    while continuar not in [1, 2]:
        continuar = int(input('\nContinuar? \n[1] - Sim   \n[2] - Não\n'))
    if continuar != 1:
        print(f'\n{"FIM":=^50}\n')
        break

print(f'\n{"Resumo":=^50}\n')
print(f'Total de Pessoas: {quantidade}')
print(f'Total de Homens: {homens}')
print(f'Mulheres com menos de 20 anos: {menosvinte}')
print(f'Pessoas com mais de 18 anos: {maisdezoito}')
