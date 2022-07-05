"""
2. def fatorial(n):
# Recebe: um inteiro n (n >= 0).
# Retorna: um inteiro com fatorial de n.
"""

def fatorial(n):
    x=n
    while n>1:
        n -= 1
        x = x*n
    return x

y = fatorial(5)
print(y)