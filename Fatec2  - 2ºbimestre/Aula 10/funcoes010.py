"""
10. def triangulo(a, b, c):
# Recebe: três valores reais a, b e c representando segmentos de reta.
# Retorna: um valor booleano indicando se os segmentos podem formar um triângulo.
"""

def triangulo(a, b, c):
    return a<b+c and b<a+c and c<a+b

tri = triangulo(3, 4, 5)
print(tri)
