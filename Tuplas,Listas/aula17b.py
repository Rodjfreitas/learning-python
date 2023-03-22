valores = []
quantidade = input('Quantos valores quer digitar na lista: ')
while quantidade.isnumeric() == False:
    quantidade = input('Quantos valores quer digitar na lista: ')
quantidade = int(quantidade)
for numero in range(0, quantidade):
    valor = input(f'Digite o {numero + 1}° número: ')
    while valor.isnumeric() == False:
        valor = input(f'Inválido. Digite o {numero + 1}° número: ')  
        valor = int(valor)
    while int(valor) in valores:
        valor = input(f'Valor Repetido. Digite o {numero + 1}° número: ')
        valor = int(valor)
    valor = int(valor)
    valores.append(valor)
print(f'\n{"Numeros Digitados":=^30}')
for pos, numero in enumerate (valores):
    print(f'número {numero} na {pos + 1}° posição.')
valores.sort()
print(f'\n{"Numeros em Ordem Crescente":=^30}')
for pos, numero in enumerate (valores):
    print(f'número {numero} na {pos + 1}° posição')
valores.sort(reverse=True)
print(f'\n{"Numeros em Ordem Decrescente":=^30}')
for pos, numero in enumerate (valores):
    print(f'número {numero} na {pos + 1}° posição.')
