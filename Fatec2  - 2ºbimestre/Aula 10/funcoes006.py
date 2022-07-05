"""
6. def tamanho(n):
# Recebe: um inteiro n (n >= 0).
# Retorna: um inteiro com a quantidade de algarismos de n.
"""

def tamanho(n):
    tam = 0
    while n>0:
        n = n//10
        tam+=1
    return tam
x = tamanho(1234567)
print(x)

