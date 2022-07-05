"""
def copia_vetor(a, b, tam):
Recebe: vetores a e b, com tam elementos cada.
Ação: copia em b os elementos de a.
"""

def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()

def copia_vetor(a, b, tam):
    for i in range(tam):
        b[i] = a[i]

a = [85, 10, 47, 54, 12]
b = 5*[0]
copia_vetor(a, b, 5)
print('b =', end=' ')
exibe(b, 5)
