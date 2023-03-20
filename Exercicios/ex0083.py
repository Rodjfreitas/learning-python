# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
expressao = input('Digite uma expressão: ')
lista = []
for v in expressao:
    lista.append(v)
if lista.count('(') == 0 and lista.count(')') == 0:
    print('Você não iniciou uma expressão!')
elif lista.count('(') == lista.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
