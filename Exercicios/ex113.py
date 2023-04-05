# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[1;31mErro! por favor Digite um valor inteiro válido:\033[m')
            continue
    


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except (ValueError, TypeError):
            print('\033[1;31mErro, por favor Digite um número real válido.\033[m')
            continue



inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real:')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')