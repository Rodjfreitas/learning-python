login = ['rodrigofreitas2011@live.com']
nome = ['Rodrigo Freitas']
senha = ['Rod@9045']
# pergunta se usuário possui cadastro
cadastro = input('\nVocê possui Cadastro?\n[1] - Sim\n[2] - Não\n:')
# valida a opção digitada para não permitir inserir um valor diferente do sugerido
while cadastro.isnumeric() == False or int(cadastro) < 1 or int(cadastro) > 2:
    cadastro = input(
        '\nVocê inseriu um valor inválido!\nVocê possui Cadastro?\n[1] - Sim\n[2] - Não\n:')
# transforma o valor digitado em número inteiro
cadastro = int(cadastro)
posicaoLogin = None
# verifica se existe usuário
if cadastro == 1:
    seulogin = str(input('\nLogin: ')).strip().lower()
    i = 0
    while i < len(login):
        if seulogin == login[i]:

            posicaoLogin = i
            existeUsuario = 'sim'
        else:
            existeUsuario = 'não'
        i += 1
    if existeUsuario == 'não':
        print('Usuário Inexistente')
    else:
        suaSenha = str(input('\nSenha: ')).strip()
        while suaSenha != senha[posicaoLogin]:
            suaSenha = str(input('\nSenha Inválida.\nSenha: ')).strip()
        print('Seja bem vindo {}'.format(nome[posicaoLogin]))
else:
    print('\nVamos Criar seu cadastro:')
    seulogin = str(input('\nDigite seu email: ')).strip().lower()
    i = 0

    while seulogin in login:
        seulogin = str(input('\nUsuário Existente\nDigite seu email: ')).strip().lower()
    
        
    login.append(seulogin)
    seuNome = str(input('\nDigite seu nome completo: ')).strip().title()
    nome.append(seuNome)            
    suaSenha = str(input('\nEscolha uma senha: ')).strip()
    while len(suaSenha) < 5:
        suaSenha = str(input('\nInválida!\nEscolha uma senha: ')).strip()
    senha.append(suaSenha)
    print('\nCadastro realizado com sucesso!')
    print('\n{}\n{}\n{}\n'.format(login, nome, senha))
    