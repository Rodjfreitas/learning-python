frase = 'Curso em Vídeo Python'

pesquisa = input('Digite:\n')
pes = len(pesquisa)
qtd = frase.find(pesquisa)

print(frase[qtd:])
print(frase.replace('Python', 'Android'))
