def soma(* num):
    soma = 0
    for valor in num:
        soma += valor
    print(soma)


soma(7, 5, 3)

# somando valores em lista (este exemplo não é pra comparar com o que foi feito acima no desempacotamento)
valores = [7, 5, 3, 5]
print(sum(valores))
