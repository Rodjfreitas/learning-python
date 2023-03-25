# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tam = len(msg)
    print("=-" * (int(tam / 2 + 1)))
    print(msg)
    print("=-" * (int(tam / 2 + 1)))

escreva('Cadastro de Pessoas Físicas')