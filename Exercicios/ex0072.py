# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostra-lo por extenso.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = input('digite um número de 1 à 20: ')
    while numero.isnumeric() == False or int(numero) < 0 or int(numero) > 20:
       numero = input('Inválido. digite um número de 1 à 20: ')
    numero = int(numero)
    print(f'\nVocê digitou o número {extenso[numero]}')
    repetir = input('\nRepetir\n[1] - Sim\n[2] - Não\n')
    while repetir not in ['1', '2']:
        repetir = input('\nRepetir\n[1] - Sim\n[2] - Não\n')
    if repetir == '2':
        break

print(f'\n{"FIM":=^50}\n')