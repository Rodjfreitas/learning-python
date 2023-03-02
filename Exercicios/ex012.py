# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Informe o preço do produto: '))
desconto = produto - (produto * 0.05)

print('O valor do produto com desconto de 5% será de R$ {:.2f}'.format(desconto))