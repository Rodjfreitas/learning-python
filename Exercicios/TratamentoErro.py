try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um erro com o tipo de dados informados')
except (ZeroDivisionError):
    print('Não é possível dividir número por zero')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre, muito obrigado.')