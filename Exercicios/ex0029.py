# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar  80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7,00 por cada km acima do limite.

print('\nVerificador de Velocidade.')
velocidade = input('\nInforme a velocidade: ').strip()
while velocidade.isnumeric() == False or int(velocidade) == 0:
    velocidade = input(
        '\nSó é permitido Numeros/Não permitido zero\nInforme a velocidade: ').strip()
velocidade = float(velocidade)
if velocidade > 80:
    print('\nVelocidade Acima do permitido.\nVocê foi MULTADO por exceder {:.0f} Km/h\nValor da Multa: R$ {:.2f}'.format(
        (velocidade - 80), (velocidade - 80) * 7))
else:
    print('Parabéns. Você está dentro da velocidade permitida para esta via.')
