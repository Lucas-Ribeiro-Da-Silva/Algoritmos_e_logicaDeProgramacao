"""
[EXEMPLO 9] Crie um programa que tenha como entrada um natural n e exiba
todos os divisores naturais de n .
"""
n = int(input('n: '))
print('Divisores de %d: ' % n)
for i in range(1, n+1):
    if n%i==0: print(i, end=' ')

"""
[EXEMPLO 10] Crie um programa que tenha como entrada um natural n e
exiba os n primeiros naturais pares.

"""
n = int(input('n: '))
print('Primeiros %d pares:' % n)
for i in range(n):
    print(2*i, end=' ')

