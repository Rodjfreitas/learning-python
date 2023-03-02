# Inserir o valor da Nota e descontar os tributos icms, pis, confins, inss, csll

notavalor = float(input('Digite o valor total da Nota fiscal: '))
pis = notavalor * 0.0165
cofins = notavalor * 0.03
csll = notavalor * 0.09
irrf = notavalor * 0.015
inss = notavalor * 0.11
icms = notavalor * 0.18
totalimpostos = pis + cofins + csll + irrf + inss + icms

print('{:=^30}'.format('NOTA FISCAL'))

print('\nValor Total: R$ {:.2f}'.format(notavalor))

print('PIS/COFINS/CSLL: {:.2F}'.format((pis + cofins + csll)))
print('IRRF: R$ {:.2f}'.format(irrf))
print('INSS: R$ {:.2f}'.format(inss))
print('ICMS: R$ {:.2f}'.format(icms))

print('Valor Líquido: R$ {:.2f}\n'.format(notavalor - totalimpostos))

print('{:=^30}'.format('='))
