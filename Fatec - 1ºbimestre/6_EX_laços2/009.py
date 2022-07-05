"""
9. [Algoritmo de Euclides] Fornecidos dois números inteiros maiores que zero, calcular o m.d.c. (máximo
divisor comum). Pesquisar no livro do FORSYTHE et al. Bibliografia 02.
"""

# não foi usado euclides, EU ACHO!
a = int(input("a?"))
b = int(input("b?"))

while b!=0:
    temp = b
    b = a % b
    a = temp
print(a)
