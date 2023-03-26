# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tam = (int(len(msg) / 2 + 1))
    print("=-" * tam)
    print(msg)
    print("=-" * tam)


escreva('Rodrigo Freitas')
