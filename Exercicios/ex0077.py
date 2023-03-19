# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). depois disso você deve mostrar para cada palavra, quais são suas vogais.
palavras = ('hoje', 'amanha', 'vida', 'amor', 'loucura', 'trabalho', 'emprego', 'ferias', 'esperanca', 'solucao', 'criador', 'youtube', 'instagram', 'facebook', 'rede social')
print(f'{"PALAVRA":<20}{"VOGAIS":<10}')
for palavra in palavras:
    print(f'\n{palavra:<20}', end='')
    for letra in palavra:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            print(f'{letra:} ', end='')
