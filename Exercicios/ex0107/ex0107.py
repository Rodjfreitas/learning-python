# Crie um módulo chamado moeda.py que tenha funções incorporadas  aumentar(), diminuir(), dobro(), e metade(). Faça também um programa que importe esse módulo e use alguma dessas funções
import moeda
numero = float(input('Digite um valor:R$ '))
reajuste = float(input('Quantos porcento deseja reajustar: '))
aumento = moeda.aumentar(numero, reajuste)
print(
    f'Aumentando o valor de {numero} reajustado à {reajuste}% será de {aumento}')
print(
    f'Diminuindo o valor de {numero} reajustado à {reajuste}% será de {moeda.diminuir(numero, reajuste)}')
print(f'A metade de {numero} é igual à {moeda.metade(numero)}')
print(f'O dobro de {numero} é igual à {moeda.dobro(numero)}')
