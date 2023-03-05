import random
# Um professor quer sortear um do seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

nome = []
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
nome.extend([aluno1, aluno2, aluno3, aluno4])

sorteio = random.randint(0, 3)
print('\nO aluno sorteado para apagar o quadro foi {}\n'.format(nome[sorteio]))