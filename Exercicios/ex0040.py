# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida - media abaixo de 5.0 reprovado - media entre 5.0 e 6.9 recuperação - media 7.0 ou superior aprovado
i = 0
notas = []
while i < 2:
    nota = float(input('Digite a nota {}: '.format(i+1)))
    while nota < 0 or nota > 10:
        nota = float(input('Digite uma nota entre 0 e 10. nota {}: '.format(i+1)))
    notas.append(nota)
    i += 1
media = (notas[0] + notas[1]) / 2
if media < 5.0:
    print('Reprovado - média: {:.1f}'.format(media))
elif media <= 6.9:
    print('Recuperação - média: {:.1f}'.format(media))
else:
    print('Aprovado - média: {:.1f}'.format(media))
