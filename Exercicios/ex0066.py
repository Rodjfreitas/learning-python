# Crie um programa que leia várias números inteiros pelo teclado. O programa só vai parar quando o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando flag)
numero = soma = quantidade = 0
print(f'{"Numeros":=^50}')
while True:
    numero = int(input('Digite um número: '))
    quantidade += 1
    if numero == 999:
        break
    soma += numero    
print('\n{:=^50}\n'.format('Resumo'))
print(f'\nSoma total: {soma}\nQuantidade de números: {quantidade}\n')