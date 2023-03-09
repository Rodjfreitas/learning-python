name = input('Digite seu nome: ')
idade = int(input('Digite sua idade '))
nascimento = 2023 - idade

# print('Olá',name + '.','Você nasceu em ',nascimento)
print('Olá \033[35;46m{}\033[m. Você nasceu em {}'.format(name, nascimento))
