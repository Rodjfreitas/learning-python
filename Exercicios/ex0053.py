# Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.
palavra = input('Digite uma palavra: ').strip().lower()
juntar = palavra.split()
novapalavra = ""
novapalavrainverso = []

for c in juntar:
    novapalavra += c

if novapalavra == novapalavra[::-1]:
    print('\nA palavra é Palíndromo.')
else:
    print('\nNão é palíndromo')
print('\na palavra normal é: {}\n'.format(novapalavra))
print('\na palavra invertida é: {}\n'.format(novapalavra[::-1]))
