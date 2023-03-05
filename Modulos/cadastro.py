cadastro = []

pergunta = int(input('Você quer adicionar um cadastro?\n[1] - Sim\n[2] - Não\n'))
if pergunta < 1 or pergunta > 2:
    pergunta = int(input('\nInválido!\nVocê quer adicionar um cadastro?\n[1] - Sim\n[2] - Não\n'))

qtd = int(input('Quantos Cadastros? '))
i = 0
if pergunta == 1:
    while i < qtd:
        nome = str(input('\nDigite o nome: '))
        cidade = str(input('Digite a cidade: '))
        nascimento = int(input('Digite o ano de nascimento: '))

        cadastro.append([nome, cidade, nascimento])
        i += 1

i = 0
while i < len(cadastro):
    print('\nNome: {} / Cidade: {} / Nascimentos: {}'.format(cadastro[i][0], cadastro[i][1], cadastro[i][2]))
    i += 1