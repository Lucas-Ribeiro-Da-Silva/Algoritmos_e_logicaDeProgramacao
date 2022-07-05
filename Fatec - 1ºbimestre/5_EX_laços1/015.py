"""
15. Dado um número inteiro 𝑛 (𝑛 > 0), calcular e exibir o maior quadrado menor ou igual a 𝑛. Exemplo:
𝑛 = 38, o maior quadrado que é menor ou igual a 38 é o 36 (6²), portanto, imprima 36. Não usar o
operador de potenciação, nenhuma função pronta e/ou conversão de tipos.
"""

#jeito n tão bom
n = int(input('n?'))
i = 1
while i * i < n:
    i+=1
if i*i>n:
    i-=1
print('Quadrado mais próximo %d' % i*i)


#jeito certo
n = int(input('n?'))
i = 1
while i * i <= n:
    i+=1
i-=1
print('Quadrado mais próximo %d' % i*i)
