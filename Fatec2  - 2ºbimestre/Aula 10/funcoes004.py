"""
4. def produto(a, b):
# Recebe: um inteiro a (a >= 0) e um inteiro b (b >= 0).
# Retorna: um inteiro com o produto de a por b.
# Obs: não usar o operador de multiplicação.
"""
def produto(a, b):
    mult = 0
    for i in range(b):
        mult += a
    return mult

prod = produto(5, 8)
print(prod)
