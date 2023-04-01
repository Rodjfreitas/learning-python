# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no 108.
import moeda
numero = float(input('Digite um valor:R$ '))
reajuste = float(input('Quantos porcento deseja reajustar: '))
while True:
    formatar = input('Formatar em moeda?\n[1] - Sim\n[2] - Não')
    if formatar in '12':
        break
    print('Inválido')
if int(formatar) == 1:
    x = True
else:
    x = False
aumento = moeda.aumentar(numero, reajuste, x)
subtracao = moeda.diminuir(numero, reajuste, x)
print(
    f'Aumentando o valor de {moeda.moeda(numero)} reajustado à {reajuste}% será de {aumento}')
print(
    f'Diminuindo o valor de {moeda.moeda(numero)} reajustado à {reajuste}% será de {subtracao}')
print(
    f'A metade de {moeda.moeda(numero)} é igual à {moeda.metade(numero, x)}')
print(
    f'O dobro de {moeda.moeda(numero)} é igual à {moeda.dobro(numero, x)}')
