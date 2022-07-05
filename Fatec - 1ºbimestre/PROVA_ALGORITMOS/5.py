"""
EXRCICIO 5
"""

n = int(input("n: "))
s = 0
for i in range (1, n):
        if n % i == 0:
            s = s + i
if s == n:
    print('perfeito')
else:
    print('não perfeito')
