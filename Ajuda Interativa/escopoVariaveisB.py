def salario(valor):
    global sal  # ao declarar globa + variavel eu peço para a função usar o valor global da variavel. se houver um calculo aqui dentro, ele executara e tornara ele global
    sal = valor * 0.08
    valor = valor - sal  # variavel sal -> escopo local
    print(f'A variavel sal vale {sal}')


# Programa principal
global sal
sal = float(input('Digite seu salário: '))  # variavel sal -> escopo global
salario(sal)
print(f'A variavel sal vale: {sal}')

# No caso acima foram declaradas duas variaveis sal: uma local (na def) e uma global (no programa principal). O valor do escopo local não influencia no escopo global, mesmo ambas tendo o mesmo nome, seus valores são distintos e não alteram um ao outro.
