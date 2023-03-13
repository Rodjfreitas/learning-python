# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos
maiorPeso = 0
menorPeso = 0
for c in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(c)))
    # Neste caso, a primeira ocorrência o valor é inserido em menor e maior.
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('\nMaior Peso {} kg\nMenor Peso {} kg'.format(maiorPeso, menorPeso))
