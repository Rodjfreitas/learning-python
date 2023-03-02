# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

mts = float(input('Digite uma metragem: '))
cm = mts * 100
mm = mts * 1000
km = mts / 1000
hm = mts / 100
dam = mts / 10
dm = mts * 10


print('{} metros equivalem à: \n{:.0f} centímetros \n{:.0f} milímetros'.format(mts, cm, mm))
print('{} metros equivalem à {:.0f} quilômetros'.format(mts, km))
print('{} metros equivalem à {:.0f} hectômetro'.format(mts, hm))
print('{} metros equivalem à {:.0f} decâmetros'.format(mts, dam))
print('{} metros equivalem à {:.0f} decímetros'.format(mts, dm))