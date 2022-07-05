"""
3. def potencia(b, e):
# Recebe: um inteiro b (b > 0) e um inteiro e (e >= 0).
# Retorna: um inteiro com a potência de b elevado a e.
# Obs: não usar o operador de potenciação ou qualquer outra função.
"""
def potencia(b, e):
        if e == 0:
            return 1
        if e == 1:
            return b
        x = b
        while e>1:
            x = x*b
            e -= 1
        return x
pot = potencia(2, 7)
print(pot)

def potencia1(c, a):
    result = c
    if a == 0:
        return 1
    for i in range(a - 1):
        mult = result*c
        result = mult
    return result
pot1 = potencia1(2, 5)
print(pot1)

