"""
[EXERCÍCIO 4] Crie um programa que leia um caractere x e um natural L, o
programa deve exibir L linhas do caractere x. A quantidade de caracteres x
por linha será decrescente de L à 1.
"""

x = input('Caractere: ')
L = int(input('Linhas: '))
for i in range(L):
    for j in range(L-i):
        print(x, end='')
    print()


"""
[EXERCÍCIO 5] Crie um programa que leia um caractere x e um natural L, o
programa deve exibir 2*L linhas do caractere x. A quantidade de caracteres x
por linha será crescente de 1 à L e, em seguida, decrescente de L à 1.
"""

