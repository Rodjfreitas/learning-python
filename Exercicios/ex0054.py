# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maior idade e quantas ja são maiores.
maiores = 0
menores = 0
for c in range(1, 7):
    nascimento = int(
        input('\nDigite o ano de nascimento da {}° pessoa: '.format(c)))
    while nascimento < 1900 or nascimento > 2023:
        nascimento = int(
            input('\nInválido.\nDigite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = 2023 - nascimento
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print('\nMaiores de idade: {} pessoas\nMenores de idade: {} pessoas.'.format(
    maiores, menores))
