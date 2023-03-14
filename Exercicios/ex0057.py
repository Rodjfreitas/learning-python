# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo: ')
while sexo not in ['f', 'F', 'm', 'M']:
    sexo = input('Inválido. Digite o sexo novamente: ')
print('Seu sexo é {}'.format(sexo).upper())