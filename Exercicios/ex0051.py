# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
pa = int(input('Digite o primeiro termo aritmético (um número qualquer): '))
razao = int(input('Digite a razão: '))
progressao = []

for c in range(0, 10):
    progressao.append(pa)
    pa += razao
print(progressao)
