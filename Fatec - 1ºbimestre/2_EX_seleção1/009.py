# 9. Fornecidos os três segmentos de reta 𝑎, 𝑏 e 𝑐 que formam um triangulo, exibir uma mensagem indicando qual o tipo de triangulo que será formado (equilátero, isósceles ou escaleno).

a = int(input("digite o valor do segmento A: "))
b = int(input("digite o valor do segmento B: "))
c = int(input("digite o valor do segmento C: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c):
    print('Equilatero')
elif (a == b) or (a == c) or (b == c):
    print('Isósceles')
else:
    print('Escaleno')