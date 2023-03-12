# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status de acordo com a tabela abaixo: abaixo de 18.5 : abaixo do peso, até 25: peso ideal, ate 30: sobrepeso, até 40: Obesidade, acima de 40: obesidade mórbida. mc = peso / altura ** 2

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc  = peso / altura ** 2

print('O IMC calculado é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você possui obesidade.')
else:
    print('Você possui obesidade mórbida.')
