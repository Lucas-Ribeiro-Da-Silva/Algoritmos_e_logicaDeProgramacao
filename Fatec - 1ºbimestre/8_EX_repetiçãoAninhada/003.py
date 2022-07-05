""""
[EXERCÍCIO 1] Crie um programa que leia dois naturais L e C e exiba L linhas com C colunas
do caractere '*'.
"""
L = int(input('Linhas: '))
C = int(input('Colunas: '))
for i in range(L):
    for j in range(C):
        print('*', end='')
    print()


"""[EXERCÍCIO 2] Crie um programa que leia um caractere x e dois naturais L e C,
o programa deve exibir L linhas com C colunas do caractere x.

"""

x = input('Caractere: ')
L = int(input('Linhas: '))
C = int(input('Colunas: '))
for i in range(L):
    for j in range(C):
        print(x, end='')
    print()

"""
[EXERCÍCIO 3] Crie um programa que leia um caractere x e um natural L, o
programa deve exibir L linhas do caractere x. A quantidade de caracteres x
por linha será crescente de 1 à L.

"""
x = input('Caractere: ')
L = int(input('Linhas: '))
for i in range(L):
    for j in range(i+1):
        print(x, end='')
    print()

