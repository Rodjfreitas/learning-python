numeros = []
quantidade = input('Quantos números você quer inserir? ')
while quantidade.isnumeric == False:
    quantidade = input('\nVocê digitou valor inválido. Quantos números você quer inserir? ')
quantidade = int(quantidade)
for numero in range(0, quantidade):
    numeros.append(int(input(f'Digite o {numero + 1}° número: ')))
numeros.sort()
print(numeros)
apagar = input('Você quer apagar algum número? ').lower()
if apagar not in 'simnao':
    apagar = input('s(sim)/n(não)? ')
if apagar in 'sim':
    numero = int(input('Digite o número que deseja apagar: '))
    if numero in numeros:
        numeros.remove(numero)
    else:
        print(f'{numero} não existe na lista')
print(numeros)