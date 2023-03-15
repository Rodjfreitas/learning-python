# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que  é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles

soma = 0
quantidade = 0
numero = int(input('\nDigite um número inteiro: '))
while numero != 999:
        soma += numero
        quantidade += 1
        numero = int(input('\nDigite outro número inteiro: '))
print('\n{:=^50}'.format('Resumo'))
print('A soma dos números digitados é {}\n'.format(soma))
print('Você digitou {} números\n'.format(quantidade))