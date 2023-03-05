import random

numeros = []

i = 0
while i < 6:
    num = random.randint(1, 60)
    numeros.append([num])
    i += 1
print(numeros)
