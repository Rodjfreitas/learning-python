# Crie um programa que vai ler vários números e colocar em uma lista. depois disso mostre 1) quantos números foram digitados 2) a lista de valores ordenada de forma decrescente 3) se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    numero = int(input(f'Digite um número: '))
    valores.append(numero)
    continuar = input('Deseja continuar? [sim/nao]\n')
    while continuar not in 'simnao':
        continuar = input('Inválido. Deseja continuar? [sim/nao]\n')
    if continuar in 'nao':
        break
valores.sort(reverse=True)
print(f'Os números inseridos foram: {valores}')
print(f'Foram digitados um total de {len(valores)} números')
if 5 in valores:
    print(f'O número 5 foi digitado {valores.count(5)} vezes')
else:
    print('Não foram encontrados número 5 na lista')
