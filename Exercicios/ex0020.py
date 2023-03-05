import random
# O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
alunos = []
aluno1 = input('Insira o nome do primeiro aluno: ')
aluno2 = input('Insira o nome do segundo aluno: ')
aluno3 = input('Insira o nome do terceiro aluno: ')
aluno4 = input('Insira o nome do quarto aluno: ')
alunos.extend([aluno1, aluno2, aluno3, aluno4])
# random.sample sorteia de forma aleatória itens dentro de array o numero e pra apresentar quantos itens sorteados
sorteio = random.sample(alunos, 4)
print('\nA ordem da apresentação será a seguinte:\n')
print('1° - {}\n2° - {}\n3° - {}\n4° - {}\n'.format((sorteio[0]), (sorteio[1]), (sorteio[2]), (sorteio[3])))