"""
1. def binario(n):
# Recebe: um inteiro n (n > 0) em decimal.
# Retorna: um inteiro com a representação binária de n.
"""
"""
def binario(n):
    x = ''
    while n > 0:
        # conversão decimal -> binário:
        resultado = n % 2
        n = n // 2
        # print(resultado, end='')
        x = str(x) + str(resultado)

    # invertendo para a ordem correta
    x = int(x)
    while x > 0:
        num = x % 10
        print(num, end='')
        x = x // 10
binario(5)
"""

def binario(n):
    inv = []
    bin = []
    while n>0:
        inv += str(n%2)
        n = n//2
        if n<=0:
            bin+=inv[::-1]
    return "".join(bin)
x = binario(9)
print(x)