# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salário superiores a 1250, calcule um aumento de 10%. Para inferiores ou iguais, aumento de 15%

salario = input('\nInforme seu salário: ').strip()

while salario.isnumeric() == False or int(salario) == 0:
    salario = input('\nValor Inválido!\nInforme seu salário: ').strip()
salario = int(salario)

if salario > 1250:
    salario = (salario * 0.10) + salario
    print('\nAumento de 10% no salário\nNovo Valor: R$ {:.2f}'.format(salario))
else:
    salario = (salario * 0.15) + salario
    print('\nAumento de 15% no salário\nNovo Valor: R$ {:.2f}'.format(salario))
