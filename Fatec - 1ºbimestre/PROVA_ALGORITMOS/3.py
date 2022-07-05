"""
EXERCICIO 3
"""
n = int(input('n: '))
d = n % 10
e = n // 10
while e > 9: e = e // 10
if e == d: print('iguais')
else: print('diferentes')
