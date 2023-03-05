import random
itens = []

nomeitens = input('\nQuais dados você quer tratar? ')

while nomeitens.isdigit() == True:
    nomeitens = input('\nInválido!\nSó permitido texto: ')

quantidade = input('\nQuantas {} diferentes você quer inserir? '.format(nomeitens))

while quantidade.isdigit() == False:
    quantidade = input('\nInválido!\nQuantas {} diferentes você que inserir? '.format(nomeitens))

print('\nVocê escolheu inserir {} {}.\n'.format(quantidade, nomeitens))
qtd = int(quantidade)
i = 0
while i < qtd:
    item = input('Digite {} de número {}: '.format(nomeitens, i + 1))
    itens.append(item)
    i += 1

listAlfabetica = sorted(itens)
print('\nOrdem Alfabética de {}:\n'.format(nomeitens))
i = 0
while i < len(itens):
    if i < 9:
        print('0{}° - {}'.format(i + 1, listAlfabetica[i]))
    else:
        print('{}° - {}'.format(i + 1, listAlfabetica[i]))
    i += 1
