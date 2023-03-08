palavra = str(input('\nDigite uma palavra: '))

qtdletras = len(palavra)

novapalavra = []

i = 0
qtd = qtdletras - 1




while i < qtdletras:
    novapalavra.insert(0, palavra[i])
    i += 1

novapalavra = ''.join(novapalavra)

palavra = palavra.upper()
novapalavra = novapalavra.upper()

if palavra == novapalavra:
    print('\nO texto é Palíndromo. normal: {} | invertido: {}\n'.format(palavra, novapalavra))
else:
    print('\nTexto não é Palíndromo. normal: {} | invertido: {}\n'.format(palavra, novapalavra))
