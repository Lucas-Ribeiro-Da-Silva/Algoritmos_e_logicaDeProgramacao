#[EXERCÍCIO 4] Crie um programa que receba dois nomes e exiba uma mensagem
#indicando se são iguais ou, caso sejam diferentes, exiba-os em ordem alfabética.

nome1 = input('nome 1:')
nome2 = input('nome 2:')

if nome1==nome2:
    print('são iguais')
else:
    if nome1<nome2:
        print(nome1)
        print(nome2)
    else:
        print(nome2)
        print(nome1)

#jeito do professoer

n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
if n1 == n2:
    print('são iguais!')
else:
    if n1 < n2:
        print('%s\n%s' % (n1, n2))
    else:
        print('%s\n%s' % (n2, n1))

#ou.................

n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
if n1 == n2:
    print('são iguais!')
elif n1 < n2:
    print('%s\n%s' % (n1, n2))
else:
    print('%s\n%s' % (n2, n1))
