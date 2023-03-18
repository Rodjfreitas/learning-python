total = quantidade = maisdemil = maisbarato = 0
produtobarato = ""
while True:
    print(f'\n{"Compra":=^40}\n')
    produto = input('Digite o nome do produto: ').strip().title()
    while len(produto) < 3:
        produto = input(
            'Qtd Caracteres inválido. Digite o nome do produto: ').strip().title()
    preco = input('Digite o preço do produto: ')
    while preco.isalpha() == True:
        preco = input('Inválido. Digite o preço do produto: ')
    total += float(preco)
    if maisbarato == 0:
        maisbarato = float(preco)
        produtobarato = produto
    else:
        if float(preco) < maisbarato:
            maisbarato = float(preco)
            produtobarato = produto
    if float(preco) > 1000:
        maisdemil += 1
    quantidade += 1
    continuar = input('\nInserir novo produto? [S / N]\n').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('\nInserir novo produto? [S / N]\n').strip().upper()
    if continuar == 'N':
        break

print(f'\n{"Resumo":=^50}\n')
print(f'Total de Lançamentos: {quantidade}\nSoma dos Lançamentos: {total:.2f}\nProdutos que Custam mais de R$ 1000: {maisdemil}\nProduto mais barato: {produtobarato} R$ {maisbarato:.2f}\n')
