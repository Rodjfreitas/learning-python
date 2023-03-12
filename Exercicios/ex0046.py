from time import sleep
import emoji
# Faça um programa que mostre na tela uma contagem regressiva para estouros de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

for c in range(10, -1, -1):
    print('\n{}'.format(c))
    print('\n...')
    sleep(1)
print(emoji.emojize("Feliz Ano Novo!!! 🎉🎉🎉", language='pt'))