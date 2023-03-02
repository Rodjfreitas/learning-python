#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

dado = input('Digite algo: ')

print('Tipo primitivo: {}'.format(type(dado)))
print('Pode ser convertido em númerico? {}'.format(dado.isnumeric()))
print('É alfabético? {}'.format(dado.isalpha()))
print('É alphanumérico? {}'.format(dado.isalnum()))
print('Todos maiúsculos? {}'.format(dado.isupper()))
print('Todos minúsculas? {}'.format(dado.islower()))
print('Só tem espaços? {}'.format(dado.isspace()))


