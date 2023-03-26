'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(5, 7)'''

# se quisear atribuir esse valor a uma variavel, faça da seguinte forma:

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


valor = somar(5, 5, 5)
print(valor)