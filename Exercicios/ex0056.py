# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre.
cadastro = []
for c in range(0, 4): 
    print('\n{:=^20}{}{}{:=^20}'.format('=', 'Cadastro n°', c + 1, '='))   
    nome = input('\nDigite o nome: ').strip().title()
    while nome.isnumeric == True or nome.count(" ") < 1:
        nome = input('\nInválido. Digite o nome completo: ').strip().title()
    nascimento = input('Qual ano de nascimento: ')
    while nascimento.isnumeric() == False or len(nascimento) != 4:
        nascimento = input('Qual ano de nascimento: ')
    idade = 2023 - int(nascimento)
    sexo = input('Qual sexo:\n[1] - Masculino\n[2] - Feminino\n')
    while sexo.isnumeric() == False or int(sexo) < 1 or int(sexo) > 2:
        sexo = input(
            '\nInválido. Qual sexo:\n[1] - Masculino\n[2] - Feminino\n')
    if int(sexo) == 1:
        sexo = 'Masculino'
    else:
        sexo = 'Feminino'
    cadastro.append([nome, nascimento, idade, sexo])

print('{:30} {:10} {:5} {:10}'.format('Nome', 'Nascimento', 'Idade', 'Sexo'))
for c in range(0, 4):    
    print('{:30} {:10} {:5} {:10}'.format(
        cadastro[c][0], cadastro[c][1], cadastro[c][2], cadastro[c][3]))
