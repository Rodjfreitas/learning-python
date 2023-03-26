def valor(b):
    #global a
    a = 5
    b += 4
    print(f'A dentro vale {a}')
    print(b)


a = 9
valor(a)
print(f'A fora vale {a}')