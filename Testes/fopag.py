aliqvt = 0
aliqinss = 0
inss = 0
aliqirrf = 0
irrf = 0
aliqfgts = 0
somadeducoes = 0
valorVA = 0
valorHE = 0
valordaHora = 0
salarioTotal = 0

# Solicita identificação
identificacao = input('Digite seu nome: ')

# Não permite que o usuário informe no nome caracteres numéricos ou alphanuméricos
while identificacao.isalnum() == True:
    print('\nNome inválido.')
    identificacao = input('Digite novamente: ')

# Questiona se possui vale transporte
optvt = int(input('\nOptante de Vale Transporte?\n[1] - Sim \n[2] - Não\n: '))

# Essa instrução não permite que seja selecionado um valor diferente de 1 ou 2 na opção vale transporte
while optvt > 2 or optvt < 1:
    print('\nOpção inválida!')
    optvt = int(input('\nOptante de Vale Transporte?\n[1] - Sim \n[2] - Não\n '))

# Se optante por vt tem desconto da alíquota de vale transporte
if optvt == 1:
    aliqvt = 0.06
else:
    aliqvt = 0

#Usuário seleciona se possui Vale alimentação
optva = int(input('\nPossui Vale Alimentação ou Refeição?\n[1] - Sim\n[2] - Não\n: '))

# Não permite digitar opção diferente das selecionadas:
while optva > 2 or optva < 1:
    print('\nOpção inválida')
    optva = int(input('\nPossui Vale Alimentação ou Refeição?\n[1] - Sim\n[2] - Não\n: '))

if optva == 1:
    va = float(input('\nInforme o Valor mensal do VA/VR: '))
    valorVA = va * 0.2    

# Pede ao usuário que informe o salário
salario = float(input('\nInforme seu salário Bruto: '))

# Calculo do valor da hora trabalhada - levando em consideração a legislação que permite 220h mensais
valordaHora = salario / 220

#Pergunta sobre existência de Hora Extras
opthe = int(input('\nRealizou Hora Extra?\n[1] - Sim\n[2] - Não\n: '))

# Não permite digitar opção diferente das selecionadas:
while opthe <  1 or opthe > 2:
    print('\nOpção Inválida')
    opthe = int(input('\nRealizou Hora Extra?\n[1] - Sim\n[2] - Não\n: '))

if opthe == 1:
    qtdhoras = float(input('\nQuantas horas foram realizadas? '))
    valorHE = (valordaHora * 1.5) * qtdhoras

salarioTotal = salario + valorHE

# FGTS
optfgts = int(input('\nInforme o tipo de contrato:\n[1] - CLT Convencional\n[2] - Contrato de Aprendizagem\n[3] - Trabalhador doméstico\n: '))

while optfgts < 1 or optfgts > 3:
    print('\nOpção Inválida')
    optfgts = int(input('\nInforme o tipo de contrato:\n[1] - CLT Convencional\n[2] - Contrato de Aprendizagem\n[3] - Trabalhador doméstico\n: '))

if optfgts == 1:
    aliqfgts = 0.08
elif optfgts == 2:
    aliqfgts = 0.02
else:
    aliqfgts = 0.112

# Calculo do INSS
if salarioTotal <= 1212:
    aliqinss = 0.075
    inss = salarioTotal * aliqinss
elif salarioTotal <= 2427.35:
    aliqinss = 0.09
    inss = 1212 * 0.075
    inss += (salarioTotal - 1212) * aliqinss
elif salarioTotal <= 3641.03:
    aliqinss = 0.12
    inss = 1212 * 0.075
    inss += (2427.35 - 1212) * 0.09
    inss += (salarioTotal - 2427.36) * aliqinss
elif salarioTotal <= 7087.22:
    aliqinss = 0.14
    inss = 1212 * 0.075
    inss += (2427.35 - 1212) * 0.09
    inss += (3641.03 - 2427.36) * 0.12
    inss += (salarioTotal - 3641.03) * aliqinss
else:
    aliqinss = 0
    inss = 0

# Calculo do IRRF
salarioirrf = salarioTotal - inss

if salarioirrf <= 1903.98:
    aliqirrf = 0
    irrf = 0
elif salarioirrf <= 2826.65:
    aliqirrf = 0.075
    irrf = (salarioirrf * aliqirrf) - 142.80
elif salarioirrf <= 3751.05:
    aliqirrf = 0.15
    irrf = (salarioirrf * aliqirrf) - 354.80
elif salarioirrf <= 4664.68:
    aliqirrf = 0.225
    irrf = (salarioirrf * aliqirrf) - 636.13
else:
    aliqirrf = 0.275
    irrf = (salarioirrf * aliqirrf) - 869.36

# Deduções
fgts = salarioTotal * aliqfgts
vt = salario * aliqvt # hora extra não entra na dedução de desconto do vt
#array com todas as deduções
deducoes = [fgts, inss, vt, irrf, valorVA]

# Somar os valores dos itens dentro do array deducoes
i = 0
while i < len(deducoes):
    somadeducoes += deducoes[i]
    i += 1

# O FGTS foi inserido nas deduções para fim de calculos matemáticos, agora tiramos pois ele não incide no líquido da folha.
saliquido = salarioTotal - (somadeducoes - fgts)

#Impressão de Resultados em tela
print('\n{:=^40}'.format('Folha de Pagamento')) # cabeçalho folha de pagamento

print('\nColaborador: {}'.format(identificacao)) # nome do colaborador
print('\n{:=^30}'.format('Receitas')) # cabeçalho deduções
print('\nSalário Bruto: R$ {:.2f}'.format(salario)) # salário bruto
print('Hora Extra Recebida: R$ {:.2f}'.format(valorHE))
print('\n{:=^30}\n'.format('Deduções')) # cabeçalho deduções
print('FGTS ({:.1f}%): R$ {:.2f}'.format((aliqfgts * 100), fgts))
if inss != 0:
    print('INSS ({:.1f}%): R$ {:.2f}'.format((aliqinss * 100), inss))
if irrf != 0:
    print('IRRF ({:.1f}%): R$ {:.2f}'.format((aliqirrf * 100), irrf))
if vt != 0:
    print('Vale Transporte: R$ {:.2f}'.format(vt))
if valorVA != 0:
    print('Vale Alimentação/Refeição: R$ {:.2f}'.format(valorVA))
print('\nTotal de Deduções: R$ {:.2f}'.format(somadeducoes))
print('\n{:=^30}\n'.format('Resumo')) 
print('Total de Receitas: R$ {:.2f}'.format(salarioTotal))
print('Total de Descontos: R$ {:.2f}'.format(somadeducoes - fgts))
print('\n{:=^30}'.format('Líquido'))
print('\nSalário Líquido: R$ {:.2f}\n'.format(saliquido))
print('\n{:=^30}\n'.format('Observações')) # cabeçalho deduções
print('> O FGTS é uma obrigação do empregador, dessa forma não incide desconto sobre a folha de pagamento.\n')
if valorHE != 0:
    print('> A hora extra foi calculada mediante adicional de 50%.\n')
    if vt != 0:
        print('> O desconto de VT não leva em consideração valor recebido por hora extra.\n')
if valorVA != 0:
    print('> A dedução do VA/VR equivale à 20% do valor depositado.\n')
if inss != 0:
    print('> A alíquota descrita acima do INSS é a máxima praticada para a remuneração informada.\n')
