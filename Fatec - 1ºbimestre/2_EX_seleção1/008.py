#8. Fornecidos os três segmentos de reta 𝑎, 𝑏 e 𝑐 (𝑎 > 0, 𝑏 > 0 e 𝑐 > 0),
# verificar se podem formar um triângulo. Exibir a mensagem 'formam' ou 'não formam', conforme o caso.

a = int(input("digite o valor do segmento A: "))
b = int(input("digite o valor do segmento B: "))
c = int(input("digite o valor do segmento C: "))

#a soma de dois lados é sempre maior que o terceiro lado

if (a+b<c) or (a+c<b) or (b+c<a):
    print('não formam')
else:
    print('formam')

"""
seleção 8
"""

"""
a = input('valor de a:')
b = input('valor de b:')
c = input('valor de c:')

if a>b and a>c:
    x = b+c
    if x>a:
        print('formam')
    else:
        print('não formam')
elif b>a and b>c:
    x = a+c
    if x>b:
        print('formam')
    else:
        print('não formam')
else:
    x = a+b
    if x>c:
        print('formam')
    else:
        print('não formam')
"""

# resolução: formam um triangulo quando:
# a<b+c   b<a+c   c<a+b
"""
a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

if a<b+c and b<a+c and c<a+b:
    print('formam')
else:
    print('não formam')
"""

"""
SELEÇÃO 9
"""

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

if a == b and b == c:
    print("equilatero")
elif a != b and b != c and c != a:
    print("escaleno")
else:
    print("isósceles")

# ou...........................................

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

if a == b and b == c:
    print('equilatero')
elif a == b or a == c or b == c:
    print(isosceles)
else:
    print('escaleno')

# agr junte os dois programas para verificar se formam e qual o tipo de triângulo

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

if a < b + c and b < a + c and c < a + b:
    print('formam')
    if a == b and b == c:
        print('equilatero')
    elif a == b or a == c or b == c:
        print('isosceles')
    else:
        print('escaleno')
else:
    print('não formam')

