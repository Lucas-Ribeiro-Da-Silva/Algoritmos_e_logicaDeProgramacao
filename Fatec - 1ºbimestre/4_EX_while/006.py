#[EXERCÍCIO 3] Crie um programa que receba dois números inteiros a e b e exiba todos os inteiros do intervalo crescente[a..b].

a = int(input('a: '))
b = int(input('b: '))
i = a
while i<=b:
    print(i, end=' ')
    i += 1
