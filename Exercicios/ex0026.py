# Faça um programa que leia uma frase pelo teclado e mostre: 1) Quantas vezes aparece a letra "A". 2) em que posição ela aparece a primeira vez. 3) Em que posição ela aparece a última vez

frase = str(input('\nDigite uma frase: '))

letraA = int(frase.count('a'))
letraA += int(frase.count('A'))
print('\nA letra A-a aparece {} vezes na frase.'.format(letraA))

qtdfrase = len(frase)
print('\nA frase possui {} caracteres.'.format(qtdfrase))

i = 0
while i < qtdfrase:
    if frase[i] == 'a' or frase[i] == 'A':
        print('\nO primeiro A-a aparece na posição {}'.format(i))
        break
    i += 1

j = qtdfrase - 1
while j >=0:
    if frase[j] == 'a' or frase[j] == 'A':
        print('\nO último A-a aparece na posição {}'.format(j))
        break
    j -= 1
