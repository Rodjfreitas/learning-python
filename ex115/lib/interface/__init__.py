def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[1;31mVocê não inseriu um valor correto. Digite novamente\033[m')
        except (KeyboardInterrupt):
            print('\033[1;31mVocê decidiu não inserir nenhum valor\033[m')
            return 0
        else:
            return valor


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
