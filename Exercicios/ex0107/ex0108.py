import moeda
numero = float(input('Digite um valor:R$ '))
reajuste = float(input('Quantos porcento deseja reajustar: '))
aumento = moeda.aumentar(numero, reajuste)
print(
    f'Aumentando o valor de {moeda.moeda(numero)} reajustado à {reajuste}% será de {moeda.moeda(aumento)}')
print(
    f'Diminuindo o valor de {moeda.moeda(numero)} reajustado à {reajuste}% será de {moeda.moeda(moeda.diminuir(numero, reajuste))}')
print(
    f'A metade de {moeda.moeda(numero)} é igual à {moeda.moeda(moeda.metade(numero))}')
print(
    f'O dobro de {moeda.moeda(numero)} é igual à {moeda.moeda(moeda.dobro(numero))}')
