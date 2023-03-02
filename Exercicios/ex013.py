# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Informe seu salário atual: '))
reajuste = (salario * 0.15) + salario

print('Seu salário será reajustado para R$ {:.2f}'.format(reajuste))
