# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
ordem = 0
maior = 0
menor = 0
quantidade = 0
soma = 0
vezes = 10
i = 0
print('\n{:=^40}'.format('Numeros Iniciais'))
while i < vezes:
    numero = int(input('digite o {}° número: '.format(ordem + 1)))
    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    soma += numero
    quantidade += 1
    ordem += 1
    if i == vezes - 1:
        opt = int(input('\nDeseja continuar inserindo números:\n[1] - Sim\n[2] - Não\n'))
        if opt == 1:
            vezes += 5
            print('\n{:=^40}'.format('Adicionando'))
        else:
            break        
    i += 1
print('\n{:=^50}'.format('Resumo'))
print('Você inseriu {} números.'.format(quantidade))
print('A soma total dos números digitados: {}'.format(soma))
print('A média dos valores digitados: {:.1f}'.format(soma / quantidade))
print('O menor valor digitado: {}\nO maior valor digitado: {}\n'.format(menor, maior))
print('{:=^50}'.format('Fim'))