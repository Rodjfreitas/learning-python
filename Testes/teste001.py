dados =[]

nome = input('Qual seu nome: ')
cidade = input('Cidade de nascimento: ')
idade = int(input('Sua idade: '))
nascimento = 2023 - idade

dados.extend([nome,cidade,idade, nascimento])


print(dados)