# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

mts = float(input('Digite uma metragem: '))
cm = mts * 100
mm = mts * 1000

print('{} metros equivalem à: \n{:.0f} centímetros \n{:.0f} milímetros'.format(mts, cm, mm))