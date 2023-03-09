cadastro = {'nome', 'sexo', 'anoNascimento', 'idade', 'cidade', 'estado'}

criar = input('Quer criar um cadastro?\n[1] - Sim\n[2] - Não\n')
while criar.isnumeric() == False or int(criar) < 1 or int(criar) > 2:
    criar = input('Você digitou um valor inválido.\nDigite novamente:\n[1] - Criar Cadastro\n[2] - Sair\n')
while int(criar) == 1:
    nome = input('\nDigite seu nome: ')
    while nome.isalnum() == True:
        nome = input('\nInválido\nDigite seu nome corretamente: ')
    cadastro.add(nome)

    criar = input('Quer criar um cadastro?\n[1] - Sim\n[2] - Não\n')
print(cadastro)