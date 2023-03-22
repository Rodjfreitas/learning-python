cadastro = input('\n[1] - Cadastrar\n[2] - Sair\n')
while True:    
    if cadastro == '1':
        nome = str(input('Digite o nome: ')).strip().title()
        idade = int(input('Sua idade: '))
        cidade = str(input('Sua cidade: ')).strip().title()
        print(f'\nOlá {nome:*<20}, você tem {idade:2} anos e mora em {cidade:20}.')      
    if cadastro == '2':
        break
    cadastro = input('\n[1] - Cadastrar\n[2] - Sair\n')
print('\n{:=^30}{}{:=^30}\n'.format('=', 'FIM', '='))