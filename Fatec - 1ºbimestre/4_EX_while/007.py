#[EXERCÍCIO 4] Crie um programa que receba dois números inteiros a e b e exiba
#todos os inteiros do intervalo crescente[a..b]. Use apenas duas variáveis.

a = int(input('a: '))
b = int(input('b: '))
while a<=b:
    print(a, end=' ')
    a += 1
