"""
9. def primo(n):
# Recebe: um inteiro n (n > 1).
# Retorna: um valor booleano indicando se n é primo.
"""
"""
def primo(n):
    cont = 0
    for i in range(1, n+1):
        if n%i==0:
            cont+=1
        if cont>2:
            return 'não é primo'
    return 'é primo'
"""
"""
def primo(n):
    qtd = 0
    for i in range(2, n):
        if n%i == 0:
            return False
        return True
"""

def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = primo(17)
print(num)