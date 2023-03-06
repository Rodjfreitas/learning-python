import openpyxl
cadastro = [['nome', 'cidade', 'nascimento']]


pergunta = int(input('Você quer adicionar um cadastro?\n[1] - Sim\n[2] - Não\n'))
if pergunta < 1 or pergunta > 2:
    pergunta = int(input('\nInválido!\nVocê quer adicionar um cadastro?\n[1] - Sim\n[2] - Não\n'))

qtd = int(input('Quantos Cadastros? '))
i = 0
if pergunta == 1:
    while i < qtd:
        nome = str(input('\nDigite o nome: ')).strip()
        cidade = str(input('Digite a cidade: ')).strip()
        nascimento = int(input('Digite o ano de nascimento: '))       

        cadastro.append([nome, cidade, nascimento])
        i += 1

i = 1
while i < len(cadastro):
    print('\nNome: {} / Cidade: {} / Nascimentos: {}'.format(cadastro[i][0], cadastro[i][1], cadastro[i][2]))
    i += 1


pergunta2 = int(input('\nGostaria de Realizar alguma pesquisa?\n[1] - Sim\n[2] - Não '))

if pergunta2 < 1 or pergunta2 > 2:
    pergunta2 = int(input('\nInválido!\nGostaria de Realizar alguma pesquisa?\n[1] - Sim\n[2] - Não \n'))

pesquisa = int(input('\nPesquisar por:\n[0] - Nome\n[1] - Cidade\n[2] - Nascimento\n'))
if pesquisa < 0 or pesquisa > 2:
    pesquisa = int(input('\nInválido!\nPesquisar por:\n[0] - Nome\n[1] - Cidade\n[2] - Nascimento\n'))
tipoPesq = input('\nDigite a Palavra chave: \n')
i = 0
if pergunta2 == 1:
    if pesquisa == 2:
        tipoPesq = int(tipoPesq)
    while i < len(cadastro):
        if tipoPesq in cadastro[i][pesquisa]:      
        #if cadastro[i][pesquisa] == tipoPesq:
            print(cadastro[i])
        i += 1

arquivo = openpyxl.Workbook()
planilha = arquivo.active



for linha in cadastro:
    planilha.append(linha)

arquivo.save('cadastroDados.xlsx')
