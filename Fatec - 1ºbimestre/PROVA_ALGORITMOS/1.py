"""
EXERCICIO 1
"""

a = int(input('a: '))
b = int(input('b: '))
m = 0
while  b > 0:
    m += a
    b -= 1
print('a * b = %d' % m)