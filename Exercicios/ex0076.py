# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia. No final mostre uma listagem de preços, organizando os dados em forma tabular
lista = (('Arroz 1Kg', 9.90), ('Feijão 1Kg', 8.66), ('Sabonete', 2.77), ('Linguiça Suína', 11.9), ('Filé de Frango', 13.80),
         ('Refrigerante', 8.28), ('Papel Higiênico', 14.98), ('Cerveja Brussels', 2.98), ('Creme dental Colgate', 7.49), ('Gilete Prestobarba', 8.00))
print(f'\n{"Supermercados Preço Bom":=^100}\n')
print(f'{"PRODUTO":<30}{"PREÇO R$":>10}')

for pos, produto in enumerate (lista):
    print(f'{produto[0]:<30}{produto[1]:>10.2f}')
print(f'\n{"=":=^100}\n')
