"""
[EXEMPLO 1] Crie um programa que exiba todos os números naturais entre 10
e 16, inclusive os extremos.
"""
for i in range(10, 17, 1):
    print(i, end=' ')

"""
[EXEMPLO 2] Crie um programa que exiba todos os números naturais pares
entre 10 e 20, inclusive os extremos.
"""
for i in range(10, 21, 2):
    print(i, end=' ')

"""
[EXEMPLO 3] Crie um programa que exiba uma contagem regressiva de 5 à 1.

"""
for i in range(5, 0, -1):
    print(i, end=' ')

"""
[EXEMPLO 4] Crie um programa que tenha como entrada dois números
inteiros a e b e exiba uma contagem progressiva de a até b.

"""
a = int(input('a: '))
b = int(input('b: '))
for i in range(a, b+1, 1):
    print(i, end=' ')

"""
[EXEMPLO 5] Crie um programa que tenha como entrada dois números
inteiros a e b e exiba uma contagem regressiva de a até b.

"""

a = int(input('a: '))
b = int(input('b: '))
for i in range(a, b-1, -1):
    print(i, end=' ')

"""
[EXEMPLO 6] Crie um programa que tenha como entrada dois números
inteiros a e b e exiba os inteiros do intervalo aberto crescente ]a..b[.

"""
a = int(input('a: '))
b = int(input('b: '))
for i in range(a+1, b, 1):
    print(i, end=' ')

"""
[EXEMPLO 7] Crie um programa que tenha como entrada três números
inteiros a, b e c e exiba os inteiros de [a..b[ pulando de c em c.
"""
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
for i in range(a, b, c):
    print(i, end=' ')

"""

"""