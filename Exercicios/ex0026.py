# Faça um programa que leia uma frase pelo teclado e mostre: 1) Quantas vezes aparece a letra "A". 2) em que posição ela aparece a primeira vez. 3) Em que posição ela aparece a última vez

frase = str(input('\nDigite uma frase: ')).strip()
corrigindo = frase.lower()

letraA = int(corrigindo.count('a'))
print('\nA letra "a" aparece {} vezes na frase.'.format(letraA))

qtdfrase = len(frase)
print('\nA frase possui {} caracteres.'.format(qtdfrase))

i = 0
while i < qtdfrase:
    if corrigindo[i] == 'a':
        print('\nO primeiro "a" aparece na posição {}\n'.format(i))
        break
    i += 1

j = qtdfrase - 1
while j >=0:
    if corrigindo[j] == 'a':
        print('\nO último "a" aparece na posição {}\n'.format(j))
        break
    j -= 1
