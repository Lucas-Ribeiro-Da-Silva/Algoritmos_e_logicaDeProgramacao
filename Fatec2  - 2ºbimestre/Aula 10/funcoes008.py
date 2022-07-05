"""
8. def nao_decrescente(n):
# Recebe: um inteiro n (n > 0).
# Retorna: um valor booleano indicando se os dígitos de n são não decrescentes.
"""

def nao_decrescente(n):
    while n>9:
        c = n % 10
        n = n // 10
        d = n % 10
        if c < d or c == d:
            return False
    return True

print(nao_decrescente(897))

