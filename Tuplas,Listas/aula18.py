cadastro = list()
dado = list()
for c in range(0, 5):
    print(f'{"=":=^20}CADASTRO {c + 1} {"=":=^20}')
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    cadastro.append(dado[:])
    dado.clear()
for valor in cadastro:
    if valor[1] > 18:
        print(f'{valor[0]} é maior de idade')
    else:
        print(f'{valor[0]} é menor de idade')
