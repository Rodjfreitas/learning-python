import openpyxl

arquivoExcel = openpyxl.load_workbook('relatorios.xlsx')

planilha = arquivoExcel['Planilha1']

nome = 'A'
nascimento = 'B'
cidade = 'C'
salario = 'D'
cargo = 'E'

lancamentos = []

for linha in planilha.iter_rows(min_row=2, values_only=True):
    valor1 = linha[0]
    valor2 = linha[1]
    valor3 = linha[2]
    valor4 = linha[3]
    valor5 = linha[4]
    lancamentos.append([valor1, valor2, valor3, valor4, valor5])


i = 0
while i < len(lancamentos):
    print('{} - {}'.format(i + 1, lancamentos[i]))
    i += 1



tip_pesq = int(input('[0] - nome\n[1] - nascimento\n[2] - cidade\n[3] - salario\n[4] - cargo\n'))
pesquisa = input('Pesquise: ')

i = 0
while i < len(lancamentos):
    if tip_pesq == 1 or tip_pesq == 3:
        pesquisa = int(pesquisa)
    
    if lancamentos[i][tip_pesq] == pesquisa:
        print(lancamentos[i])
    i += 1