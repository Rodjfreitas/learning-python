# Crie um módulo chamado moeda.py que tenha funções incorporadas  aumentar(), diminuir(), dobro(), e metade(). Faça também um programa que importe esse módulo e use alguma dessas funções
import moeda
numero = float(input('Digite um valor:R$ '))
reajuste = float(input('Quantos porcento deseja reajustar: '))
aumento = moeda.aumentar(numero, reajuste)
print(f'O valor de R${numero:.2f} reajustado à {reajuste}% será de R${aumento:.2f}')
print(f'Se fosse para diminuir, o valor de reajuste seria R${moeda.diminuir(numero, reajuste):.2f}')
print(f'A metade de {numero:.0f} é igual à {moeda.metade(numero):.0f}')
print(f'O dobro de {numero:.0f} é igual à {moeda.dobro(numero):.0f}')