"""
5. def divisao(p, q):
# Recebe: um inteiro p (p >= 0) e um inteiro q (q > 0).
# Retorna: um inteiro com o quociente da divisão inteira de p por q.
# Obs: não usar os operadores de divisão e/ou multiplicação.
"""
def divisao(p, q):
    if q == 0:
        return 'Não é possível dividir por 0'
    result = 0
    while p>=q:
        result += 1
        p -= q
    return result
div = divisao(127, 5)
print(div)


