#[EXEMPLO 5] Crie um programa que receba um número natural n (n>1) e exiba uma mensagem indicando se n é primo.

n = int(input('n: '))
d = 2
while d < n:
    if n%d == 0:
        break
    d += 1
if d==n:
    print('Primo')
else:
    print('Não primo')
