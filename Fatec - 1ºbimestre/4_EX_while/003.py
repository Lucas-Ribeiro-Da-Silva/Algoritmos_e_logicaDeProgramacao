#[EXERCÍCIO 2] Crie um programa que receba um número inteiro n (n>0) e exiba
# os dígitos de n da direita para a esquerda.

n = int(input('n: '))
while n > 0:
    print(n % 10, end='')
    n = n // 10

