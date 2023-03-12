# Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.
palavra = input('Digite uma palavra: ').strip().lower()
juntar = palavra.split()
novapalavra = ""
novapalavrainverso = []

for c in juntar:
    novapalavra += c

if novapalavra == novapalavra[::-1]:
    print('A palavra é Palíndromo.')
else:
    print('Não é palíndromo')

print(novapalavra[::-1])   
print(novapalavra)